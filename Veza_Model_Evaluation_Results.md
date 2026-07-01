# Veza — Model Evaluation Results (completed)

**Goal:** Test whether an off-the-shelf AI translation model (Google Translate) preserves the meaning of scam-reporting and safety-critical phrases in isiZulu and Sesotho. This supports Veza's design choice to keep a human in the loop rather than trust automated translation for safety-critical text.

**Method:** Back-translation round-trip. Each English phrase was translated to the target language, then translated back to English. The round-trip English was compared to the original to judge whether meaning was preserved. A native speaker was not available in time, so the team used this back-translation method to check the translations.

**Model:** Google Translate | **Test set:** 12 phrases per language (24 total)

**Rating scale:** Correct (meaning preserved) · Partial (gist preserved, detail lost) · Wrong (meaning changed) · Hallucinated (invented content)

---

## isiZulu

| # | English original | isiZulu (Google Translate) | Round-trip English | Rating |
|---|---|---|---|---|
| 1 | The caller said my bank account was frozen and I must verify my PIN. | Oshaye ucingo uthe i-akhawunti yami yasebhange ivaliwe futhi kumele ngiqinisekise i-PIN yami. | The caller said my bank account was closed and I needed to verify my PIN. | Partial (frozen to closed) |
| 2 | A video showed a famous doctor selling medicine that cures everything. | Ividiyo ibonise udokotela odumile ethengisa umuthi olapha yonke into. | The video showed a famous doctor selling a cure-all. | Correct |
| 3 | They promised I would double my money in one week. | Bathembise ukuthi ngizophinda kabili imali yami ngesonto elilodwa. | They promised to double my money in one week. | Correct |
| 4 | Someone pretending to be the police said I would be arrested today. | Othile ozenza amaphoyisa uthe ngizoboshwa namuhla. | Someone pretending to be a police officer said I would be arrested today. | Correct |
| 5 | I received a one-time PIN and they asked me to read it to them. | Ngithole i-PIN yesikhathi esisodwa futhi bangicela ukuba ngibafundele yona. | I received a one-time PIN and they asked me to read it to them. | Correct |
| 6 | The voice on the phone sounded like a robot, not a real person. | Izwi efonini lalizwakala njengerobhothi, hhayi umuntu wangempela. | The voice on the phone sounded like a robot, not a real person. | Correct |
| 7 | A message offered me a job but asked for a registration fee first. | Umlayezo wanginika umsebenzi kodwa wangicela imali yokubhalisa kuqala. | The message offered me a job but asked me to pay for registration first. | Correct |
| 8 | They sent a link and told me to click it to claim my prize. | Bathumele isixhumanisi bangitshela ukuthi ngisichofoze ukuze ngithole umklomelo wami. | They sent me a link and told me to click it to get my prize. | Correct |
| 9 | My grandmother lost money after a fake call from someone sounding like her son. | Ugogo wami ulahlekelwe yimali ngemuva kocingo oluyimbumbulu oluvela kothile ozwakala njengendodana yakhe. | My grandmother lost money after a fake call from someone who pretended to be her son. | Partial (sounding like to pretended to be) |
| 10 | The investment company is not registered and guarantees thirty percent returns. | Inkampani yokutshala imali ayibhalisiwe futhi iqinisekisa imbuyiselo engama-30%. | The investment company is not registered and guarantees a 30% return. | Correct |
| 11 | I think the photo of the minister endorsing the scheme was fake. | Ngicabanga ukuthi isithombe sikangqongqoshe esekela lolu hlelo sasiyimbumbulu. | I think the picture of the minister supporting the scheme was fake. | Correct |
| 12 | They asked me to pay using vouchers instead of a bank transfer. | Bangicele ukuthi ngikhokhe ngisebenzisa ama-voucher esikhundleni sokudlulisa imali ebhange. | They asked me to pay using vouchers instead of bank transfer. | Correct |

**isiZulu tally:** Correct 10 · Partial 2 · Wrong 0 · Hallucinated 0

---

## Sesotho

| # | English original | Sesotho (Google Translate) | Round-trip English | Rating |
|---|---|---|---|---|
| 1 | The caller said my bank account was frozen and I must verify my PIN. | Moletsi o itse ak'haonte ya ka ya banka e thibilwe mme ke tlameha ho netefatsa PIN ya ka. | The caller said my bank account was blocked and I had to verify my PIN. | Partial (frozen to blocked) |
| 2 | A video showed a famous doctor selling medicine that cures everything. | Video e bontshitse ngaka e tummeng e rekisang meriana e fodisang ntho e nngwe le e nngwe. | The video showed a famous doctor selling cure-all medicines. | Correct |
| 3 | They promised I would double my money in one week. | Ba tshepisitse hore ke tla imena habeli tjhelete ya ka ka beke e le nngwe. | They promised to double my money in one week. | Correct |
| 4 | Someone pretending to be the police said I would be arrested today. | Motho e mong ya iketsang sepolesa o itse ke tla tshwarwa kajeno. | Someone pretending to be a police officer said I would be arrested today. | Correct |
| 5 | I received a one-time PIN and they asked me to read it to them. | Ke fumane PIN ya hang feela mme ba nkopa hore ke ba balle yona. | I got a one-time PIN and they asked me to read it to them. | Correct |
| 6 | The voice on the phone sounded like a robot, not a real person. | Lentswe fonong le ne le utlwahala jwalo ka roboto, eseng motho wa sebele. | The voice on the phone sounded like a robot, not a real person. | Correct |
| 7 | A message offered me a job but asked for a registration fee first. | Molaetsa o ile wa mpha mosebetsi empa wa kopa tefiso ya ngodiso pele. | The message offered me a job but asked for a registration fee first. | Correct |
| 8 | They sent a link and told me to click it to claim my prize. | Ba ile ba romela sehokelo mme ba mpolella hore ke se tobetse ho fumana moputso wa ka. | They sent a link and told me to click on it to get my reward. | Correct |
| 9 | My grandmother lost money after a fake call from someone sounding like her son. | Nkgono o lahlehetsoe ke chelete ka mor'a mohala oa bohata o tsoang ho motho ea utloahalang joaloka mora oa hae. | Grandma lost money after a fake call from someone who sounded like her son. | Correct |
| 10 | The investment company is not registered and guarantees thirty percent returns. | Khamphani ea matsete ha e ngolisoe 'me e tiisa phaello ea mashome a mararo lekholong. | The investment company is not registered and guarantees a thirty percent return. | Correct |
| 11 | I think the photo of the minister endorsing the scheme was fake. | Ke nahana hore foto ea letona le tšehetsang morero ona e ne e le ea bohata. | I think the photo of the minister supporting the project was fake. | Correct |
| 12 | They asked me to pay using vouchers instead of a bank transfer. | Ba ile ba nkopa hore ke lefe ke sebelisa li-voucher ho e-na le phetisetso ea banka. | They asked me to pay using vouchers instead of bank transfer. | Correct |

**Sesotho tally:** Correct 11 · Partial 1 · Wrong 0 · Hallucinated 0

---

## Overall result

| | Correct | Partial | Wrong | Hallucinated |
|---|---|---|---|---|
| isiZulu | 10 | 2 | 0 | 0 |
| Sesotho | 11 | 1 | 0 | 0 |
| **Total / 24** | **21** | **3** | **0** | **0** |

**About 21 of 24 phrases (88%) kept their full meaning.** No hallucinations occurred on this clean written test set.

## A separate, important failure (found in the live bot strings)

The test set above uses complete sentences, where meaning held up well. But a separate check of Veza's own interface strings found a real failure in a short instruction: the phrase "reply SKIP to finish" was mistranslated in Sesotho so that the action word "skip" was confused with "be careful / take care." A user following the translated instruction would not know how to skip the step. This is a functional failure of a usability and safety instruction caused by automated translation.

## What this shows

Automated translation handled general sentence meaning well on clean text, but it is weaker on short, precise, functional instructions, which is exactly the content where an error is most harmful. This is also the easy case: real reports are spoken, mixed-language, and in different dialects, where automated tools are known to perform worse. This supports Veza's design choice to keep a human in the loop for safety-critical strings and for reviewing voice notes, rather than relying on automated translation.

## Limitations of this evaluation

Single model; small sample (24 phrases); clean written text only; back-translation is an imperfect proxy because an error can happen in either direction; checked by the team using back-translation rather than by a native speaker. This is an indicative finding, not a full benchmark. A fuller study would test more models, use native-speaker review, and test real spoken and mixed-language input.
