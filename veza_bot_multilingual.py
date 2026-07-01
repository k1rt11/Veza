"""
Veza — Multilingual WhatsApp reporting bot (Twilio + Flask)
===========================================================
English / isiZulu / Sesotho. The user picks a language and the whole flow
responds in that language.

PRIVACY: the sender's phone number is NEVER stored. Each report gets a random
report_id; the number is only hashed in-memory to hold the conversation.
"""

import os
import csv
import uuid
import hashlib
from datetime import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

CSV_FILE = "reports.csv"
CSV_HEADER = ["report_id", "timestamp", "language", "harm_type", "channel",
              "impact", "reported_before", "free_text_summary", "has_evidence"]
sessions = {}


def sid(n):
    return hashlib.sha256(n.encode()).hexdigest()[:16]


def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(CSV_HEADER)


def save_report(s):
    ensure_csv()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            uuid.uuid4().hex[:10],
            datetime.utcnow().isoformat(timespec="seconds"),
            s.get("language", ""), s.get("harm_type", ""), s.get("channel", ""),
            s.get("impact", ""), s.get("reported_before", ""),
            s.get("free_text_summary", ""), s.get("has_evidence", "no"),
        ])


# =====================  MESSAGE SETS  ========================================
# T[lang][key]. lang in {en, zu, st}

WELCOME = (
    "👋 You're not alone, and this is not your fault. / Awuwedwa / Ha o mong.\n\n"
    "Reply with a number to choose your language:\n"
    "1 — English\n2 — isiZulu\n3 — Sesotho"
)

T = {
    "en": {
        "screen": ("Did this involve a *fake voice, image, video, or automated "
                   "messages that did not seem human*?\n\n1 — Yes\n2 — No / Not sure"),
        "not_ai": ("Thank you. Veza focuses on AI-related scams (like deepfakes or "
                   "voice clones), so this may be outside what we collect — but you can "
                   "still get help.\n\nTo report any scam or get advice, call the free "
                   "Yima hotline: *083 123 7226*.\n\nStay safe. 💛"),
        "q1": ("What kind of scam was it? Reply with a number:\n"
               "1 — Impersonation (someone pretended to be a person or company)\n"
               "2 — Deepfake (fake video or photo of a real person)\n"
               "3 — Fake investment or \"get rich\" offer\n"
               "4 — Fake job or work offer\n5 — False information / fake news\n"
               "6 — Something else"),
        "q2": ("Where did it happen? Reply with a number:\n1 — WhatsApp\n2 — Phone call\n"
               "3 — Facebook\n4 — Email or SMS\n5 — Somewhere else"),
        "q3": ("What did it affect? Reply with a number:\n1 — I lost money\n"
               "2 — I gave away personal information\n3 — It upset me but I lost nothing\n"
               "4 — Nothing happened, I caught it in time"),
        "q4": ("Did you report this anywhere else?\n1 — Yes\n2 — No, I felt ashamed\n"
               "3 — No, I didn't know where to report\n4 — No, I didn't think it would help"),
        "q5": ("Last step (optional). Send a screenshot or voice note, OR type what "
               "happened in your own words, OR reply SKIP to finish.\nThis part helps "
               "most — tell us what happened."),
        "next_core": ("✅ Thank you. Your report is recorded and helps protect your "
                      "community.\n\n*What to do now:*\n• Call the free Yima hotline: "
                      "*083 123 7226*.\n• If you lost money or shared banking details, call "
                      "your bank's fraud line immediately and freeze affected cards.\n"
                      "• Do not click any more links. Block and delete the contact.\n"
                      "• Protect yourself for free at www.safps.org.za."),
        "rf": {
            "impersonation": ("*Spot it next time:* Real banks, SARS and police NEVER ask "
                              "for your PIN, password or OTP, and never \"investigate\" over "
                              "WhatsApp. If someone rushes you, call the company on their "
                              "official number."),
            "deepfake": ("*Spot it next time:* A video or voice can be faked. If a known "
                         "person asks for money or promotes an investment, treat it as fake "
                         "until proven real — call them on a trusted number."),
            "investment": ("*Spot it next time:* No real investment \"guarantees\" 30% "
                           "returns. Guaranteed profit + pressure to deposit fast = scam. "
                           "Check the company is FSCA-registered first."),
            "job": ("*Spot it next time:* A real employer never asks you to PAY for a job, "
                    "training or fees, or for your banking PIN. Upfront costs = almost always "
                    "a scam."),
            "falseinfo": ("*Spot it next time:* Fake news and AI posts spread fast. Before "
                          "forwarding something shocking, check a trusted news source reports "
                          "the same thing."),
            "other": ("*Spot it next time:* If a message creates urgency, asks for money or "
                      "details, or seems too good to be true — pause and verify through an "
                      "official channel first."),
        },
        "digest": ("Want a free weekly WhatsApp message on the latest scams and how to spot "
                   "them?\n\n1 — Yes\n2 — No thanks"),
        "done_yes": "Done! Stay safe. 💛 (Reply STOP anytime to unsubscribe.)",
        "done_no": "No problem. Stay safe. 💛 Your number is not stored.",
    },

    "zu": {
        "screen": ("Ingabe lokhu kwakuhilela izwi, isithombe, ividiyo, noma imiyalezo "
                   "ezenzakalelayo engabonakali njengomuntu?\n\n1 — Yebo\n2 — Cha / Angiqiniseki"),
        "not_ai": ("Ngiyabonga. I-Veza igxile ekukhwabaniseni okuhlobene ne-AI (njenge-"
                   "deepfakes noma ama-clone ezwi), ngakho lokhu kungase kube ngaphandle "
                   "kwalokho esikuqoqayo — kodwa usengathola usizo.\n\nUkubika noma yikuphi "
                   "ukukhwabanisa, shayela ucingo lwamahhala lwe-Yima: *083 123 7226*.\n\n"
                   "Hlala uphephile. 💛"),
        "q1": ("Hlobo luni lokukhwabanisa? Phendula ngenombolo:\n"
               "1 — Ukuzenza ongeyena (othile uzenze umuntu noma inkampani)\n"
               "2 — Deepfake (ividiyo noma isithombe somuntu wangempela)\n"
               "3 — Ukutshalwa kwezimali okungamanga noma isiphakamiso \"sokuceba\"\n"
               "4 — Umsebenzi noma isiphakamiso somsebenzi esingamanga\n"
               "5 — Ulwazi olungamanga / izindaba ezingamanga\n6 — Okunye"),
        "q2": ("Kwenzeke kuphi? Phendula ngenombolo:\n1 — WhatsApp\n2 — Ucingo\n3 — Facebook\n"
               "4 — I-imeyili noma i-SMS\n5 — Kwenye indawo"),
        "q3": ("Kuthinte ini? Phendula ngenombolo:\n1 — Ngilahlekelwe yimali\n"
               "2 — Ngikhiphe ulwazi lomuntu siqu\n3 — Kwangicasula kodwa angilahlekelwanga lutho\n"
               "4 — Akukho okwenzekile, ngikubambe ngesikhathi"),
        "q4": ("Ingabe ukubike lokhu kwenye indawo?\n1 — Yebo\n2 — Cha, ngazizwa nginamahloni\n"
               "3 — Cha, ngangingazi ukuthi ngizobika kuphi\n4 — Cha, ngangingacabangi ukuthi "
               "kuzosiza"),
        "q5": ("Isinyathelo sokugcina (ongakukhetha). Thumela isithombe-skrini noma inothi "
               "yezwi, NOMA uthayiphe okwenzekile ngamazwi akho, NOMA uphendule u-SKIP ukuze "
               "uqede. Noma yini oyabelana ngayo iyasiza ekuxwayiseni abanye."),
        "next_core": ("✅ Ngiyabonga. Umbiko wakho uyaqoshwa futhi usiza ekuvikeleni umphakathi "
                      "wakho.\n\n*Okufanele ukwenze manje:*\n• Shayela ucingo lwamahhala lwe-"
                      "Yima: *083 123 7226*.\n• Uma ulahlekelwe yimali noma wabelane "
                      "ngemininingwane yasebhange, shayela ucingo lokukhwabanisa lwebhange "
                      "lakho ngokushesha bese uvala amakhadi.\n• Ungachofozi ezinye "
                      "izixhumanisi. Vimba ususe oxhumana naye.\n• Zivikele mahhala ku-"
                      "www.safps.org.za."),
        "rf": {
            "impersonation": ("*Yibone ngokuzayo:* Amabhange angempela, i-SARS, namaphoyisa "
                              "NGEKE bacele i-PIN yakho, iphasiwedi, noma i-OTP, futhi ngeke "
                              "benze \"uphenyo\" nge-WhatsApp. Uma othile ekuphuthuma, shayela "
                              "inkampani enombolweni yayo esemthethweni."),
            "deepfake": ("*Yibone ngokuzayo:* Ividiyo noma izwi lingaqanjwa amanga. Uma umuntu "
                         "owaziwayo ecela imali noma ekhuthaza ukutshalwa kwezimali, kuphathe "
                         "njengamanga kuze kufakazelwe. Shayela umuntu wangempela enombolweni "
                         "oyethembayo."),
            "investment": ("*Yibone ngokuzayo:* Azikho iziqinisekiso \"zokutshalwa kwezimali\" "
                           "ezibuyisa u-30%. Inzuzo eqinisekisiwe + ukuphoqa ukuthi ufake imali "
                           "ngokushesha = inkohliso. Hlola ukuthi inkampani ibhalisiwe yini ne-"
                           "FSCA kuqala."),
            "job": ("*Yibone ngokuzayo:* Umqashi wangempela ngeke akucele ukuthi UKHOKHELE "
                    "umsebenzi, ukuqeqeshwa, noma izimali, noma i-PIN yakho yasebhange. Izindleko "
                    "zangaphambilini = cishe njalo inkohliso."),
            "falseinfo": ("*Yibone ngokuzayo:* Izindaba ezingamanga nokuthunyelwe okukhiqizwe "
                          "yi-AI kusakazeka ngokushesha. Ngaphambi kokuthumela into eshaqisayo, "
                          "hlola ukuthi umthombo wezindaba othembekile ubika into efanayo."),
            "other": ("*Yibone ngokuzayo:* Uma umlayezo udala ukuphuthuma, ucela imali noma "
                      "imininingwane, noma ubonakala umuhle kakhulu — misa isikhashana "
                      "uqinisekise ngesiteshi esisemthethweni kuqala."),
        },
        "digest": ("Ufuna umlayezo wamahhala we-WhatsApp wamasonto onke obonisa ukukhwabanisa "
                   "kwakamuva nokuthi ungakubona kanjani?\n\n1 — Yebo\n2 — Cha ngiyabonga"),
        "done_yes": ("Kwenziwe! Hlala uphephile. 💛 (Phendula u-STOP noma nini ukuze "
                     "uzikhiphe.)"),
        "done_no": "Akunankinga. Hlala uphephile. 💛 Inombolo yakho ayigcinwanga.",
    },

    "st": {
        "screen": ("Na see se ne se kenyeletsa lentswe, setshwantsho, video, kapa melaetsa "
                   "ya bohata e neng e sa bonahale e le ya batho?\n\n1 — E\n2 — Tjhe / Ha ke na "
                   "bonnete"),
        "not_ai": ("Ke a leboha. Veza e shebane le bosholu bo amanang le AI (jwalo ka di-"
                   "deepfake kapa di-voice clone), kahoo sena se ka ba kantle ho seo re se "
                   "bokellang — empa o ntse o ka fumana thuso.\n\nHo tlaleha bosholu bofe kapa "
                   "bofe, letsetsa mohala wa mahala wa Yima: *083 123 7226*.\n\nLula o "
                   "bolokehile. 💛"),
        "q1": ("E ne e le bosholu ba mofuta ofe? Araba ka nomoro:\n"
               "1 — Boiketsiso (motho o iketselitse eka ke motho kapa k'hamphani)\n"
               "2 — Deepfake (video kapa foto ya bohata ya motho wa nnete)\n"
               "3 — Tlhahiso ya matsete a bohata kapa ya \"ho ruang\"\n"
               "4 — Tlhahiso ya mosebetsi ya bohata\n5 — Tlhahisoleseling ya bohata / litaba "
               "tsa bohata\n6 — Ntho e nngwe"),
        "q2": ("E etsahetse hokae? Araba ka nomoro:\n1 — WhatsApp\n2 — Mohala\n3 — Facebook\n"
               "4 — Imeile kapa SMS\n5 — Sebakeng se seng"),
        "q3": ("E amme eng? Araba ka nomoro:\n1 — Ke lahlehetswe ke chelete\n"
               "2 — Ke fane ka tlhahisoleseling ya botho\n3 — E nkutloisitse bohloko empa ha "
               "kea lahleheloa ke letho\n4 — Ha ho letho le etsahetseng, ke e tshwere ka nako"),
        "q4": ("Na o tlalehile sena kae kapa kae?\n1 — E\n2 — Tjhe, ke ile ka ikutloa ke "
               "hlajoa ke lihlong\n3 — Tjhe, ke ne ke sa tsebe moo nka tlalehang teng\n"
               "4 — Tjhe, ke ne ke sa nahane hore e tla thusa"),
        "q5": ("Mohato wa ho qetela (ha ho hlokahale). O ka romela setshwantsho sa skrine "
               "kapa molaetsa wa lentswe, KAPA o thaepa se etsahetseng ka mantswe a hao, KAPA "
               "o arabe SKIP ho qeta. Ntho efe kapa efe eo o e arolelanang e thusa ho lemosa "
               "ba bang."),
        "next_core": ("✅ Ke a leboha. Tlaleho ya hao e rekotilwe mme e thusa ho sireletsa "
                      "setjhaba sa heno.\n\n*Seo o lokelang ho se etsa jwale:*\n• Letsetsa "
                      "mohala wa mahala wa Yima: *083 123 7226*.\n• Haeba o lahlehetswe ke "
                      "tjhelete kapa o arolelane dintlha tsa banka, letsetsa mohala wa "
                      "bolotsana wa banka ya hao hanghang.\n• O se ke wa tobetsa dihokelo tse "
                      "ding. Thibela mme o hlakole motho eo.\n• Itshireletse mahala ho "
                      "www.safps.org.za."),
        "rf": {
            "impersonation": ("*E bone nakong e tlang:* Dibanka tsa nnete, SARS, le mapolesa "
                              "HA BA KOPE PIN ya hao, phasewete, kapa OTP, mme ba ke ke ba "
                              "etsa \"dipatlisiso\" ka WhatsApp. Haeba motho a o potlakela, "
                              "letsetsa khamphani ka nomoro ya yona ya semmuso."),
            "deepfake": ("*E bone nakong e tlang:* Video kapa lentswe le ka etsoa leshano. "
                         "Haeba motho ya tsejoang a kopa chelete kapa a khothalletsa letsete, "
                         "le nke e le leshano ho fihlela le pakoa. Letsetsa motho wa nnete ka "
                         "nomoro eo o e tshepang."),
            "investment": ("*E bone nakong e tlang:* Ha ho na litiisetso tsa nnete tse "
                           "khutlisang 30%. Phaello e tiisitsoeng + khatello ya ho kenya "
                           "chelete kapele = bolotsana. Hlahloba hore na k'hamphani e "
                           "ngolisitsoe le FSCA pele."),
            "job": ("*E bone nakong e tlang:* Mohiri wa nnete a ke ke a o kopa ho LEFA "
                    "mosebetsi, koetliso, kapa litefiso, kapa PIN ya hao ya banka. Litshenyehelo "
                    "tsa pele = hoo e batlang e le kamehla ke bolotsana."),
            "falseinfo": ("*E bone nakong e tlang:* Litaba tsa bohata le lingoliloeng tse "
                          "hlahisoang ke AI li ata kapele. Pele o fetisetsa ntho e tshosang, "
                          "hlahloba hore na mohloli o tshepahalang o tlaleha ntho e tshwanang."),
            "other": ("*E bone nakong e tlang:* Haeba molaetsa o baka potlako, o kopa chelete "
                      "kapa dintlha, kapa o bonahala o le motle haholo — ema hanyane o netefatse "
                      "ka kanale ya semmuso pele."),
        },
        "digest": ("Na o batla molaetsa wa mahala wa WhatsApp wa beke le beke o bontshang "
                   "bosholu ba moraorao le hore na o ka bo bona jwang?\n\n1 — E\n2 — Tjhe ke a "
                   "leboha"),
        "done_yes": ("E se e entswe! Lula o bolokehile. 💛 (Araba STOP neng kapa neng ho "
                     "itlhakola.)"),
        "done_no": "Ha ho bothata. Lula o bolokehile. 💛 Nomoro ya hao ha e a bolokwa.",
    },
}

HARM_MAP = {"1": "impersonation", "2": "deepfake", "3": "investment",
            "4": "job", "5": "falseinfo", "6": "other"}
CHAN_MAP = {"1": "whatsapp", "2": "call", "3": "facebook", "4": "email_sms", "5": "other"}
IMPACT_MAP = {"1": "money", "2": "data", "3": "distress", "4": "caught_in_time"}
REPORTED_MAP = {"1": "yes", "2": "shame", "3": "didnt_know", "4": "didnt_think_help"}


@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    body = (request.values.get("Body", "") or "").strip()
    from_number = request.values.get("From", "")
    num_media = int(request.values.get("NumMedia", 0))
    key = sid(from_number)
    resp = MessagingResponse()
    s = sessions.get(key)

    if s is None:
        sessions[key] = {"step": "lang"}
        resp.message(WELCOME)
        return str(resp)

    lang = s.get("language", "en")
    t = T.get(lang, T["en"])
    step = s["step"]

    if step == "lang":
        s["language"] = {"1": "en", "2": "zu", "3": "st"}.get(body, "en")
        t = T[s["language"]]
        s["step"] = "screen"
        resp.message(t["screen"])

    elif step == "screen":
        if body == "1":
            s["step"] = "q1"
            resp.message(t["q1"])
        else:
            resp.message(t["not_ai"])
            sessions.pop(key, None)

    elif step == "q1":
        s["harm_type"] = HARM_MAP.get(body, "other")
        s["step"] = "q2"
        resp.message(t["q2"])

    elif step == "q2":
        s["channel"] = CHAN_MAP.get(body, "other")
        s["step"] = "q3"
        resp.message(t["q3"])

    elif step == "q3":
        s["impact"] = IMPACT_MAP.get(body, "")
        s["step"] = "q4"
        resp.message(t["q4"])

    elif step == "q4":
        s["reported_before"] = REPORTED_MAP.get(body, "")
        s["step"] = "q5"
        resp.message(t["q5"])

    elif step == "q5":
        if num_media > 0:
            s["has_evidence"] = "yes"
            s["free_text_summary"] = "[media submitted — pending human review]"
        elif body.upper() == "SKIP":
            s["free_text_summary"] = ""
        else:
            s["free_text_summary"] = body[:300]
        save_report(s)
        s["step"] = "digest"
        resp.message(t["next_core"] + "\n\n" + t["rf"][s["harm_type"]])
        resp.message(t["digest"])

    elif step == "digest":
        resp.message(t["done_yes"] if body == "1" else t["done_no"])
        sessions.pop(key, None)

    else:
        sessions.pop(key, None)
        resp.message(WELCOME)

    return str(resp)


@app.route("/", methods=["GET"])
def health():
    return "Veza bot is running.", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
