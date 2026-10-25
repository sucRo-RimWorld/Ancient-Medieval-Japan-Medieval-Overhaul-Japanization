> **Authority:** This repository is now the authoritative owner of Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）. Project-level copies are migration history only and must not evolve independently.

# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） — Design

**Status:** dedicated owner repository active; initial implementation planning (Project pre-split history migrated here).

The concept is defined, but there is no dedicated owner repository yet. Project owns the evolving pre-split design.

**2026-10-25 MO東洋系ニンジン・日本カボチャの説明案（歴史文言の作者採否待ち）:** Agriculture [PR #254](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Agriculture/pull/254) の植物系統に合わせ、既存MO `DankPyon_Plant_Carrots`／`DankPyon_RawCarrots`／`DankPyon_Plant_Pumpkins`／`DankPyon_RawPumpkins` の英日descriptionだけを候補として`Patches/Production/JapanizeMOCarrotPumpkinDescriptions.xml`および`Languages/Japanese/DefInjected/ThingDef/MO_CarrotPumpkinDescriptions.xml`に用意する。ニンジンは東洋系の長い根と16世紀末～17世紀伝来、日本カボチャは16世紀伝来・西洋種より水分が多く甘味は控えめ、と史料を越えない短文に限定。既存MO本体・日本語翻訳Mod`Lucifel.MedievalOH.JPT`の元説明を原本1.6 ZIPで確認済み。既存の日本語label、英語label、DefName、研究、種・生育・収量・低温・腐敗・栄養・料理Recipe、画像（作者指定でスキップ）、`loadAfter`は変更しない。既存画像の形態が歴史系統に一致するという主張ではない。**これはDraft PRの文言案であり、作者による表現の採否が確定するまでmainに反映しない。** 原本XPath4/4、翻訳元キー4/4、XML構造の静的照合のみ。元RimWorld 1.6の最終表示とMO日本語翻訳併用・旧セーブ・1.7は未検証。参照：<https://vegetable.alic.go.jp/yasaijoho/yasai/0502_yasai1.html>、<https://vegetable.alic.go.jp/yasaijoho/yasai/2308_yasai1.html>。研究解禁の時代別変更はAgricultureや全研究順の検討に譲り、本件で変更しない。

**2026-10-24 MOリンゴの文字情報のみ和リンゴ化・研究表示修正（画像スキップ）:** 原本MO 1.6.2.2は果樹`DankPyon_Tree_Apple`の栽培研究`Cocoa`と桑`DankPyon_Tree_Mulberry`の栽培研究`Cocoa`を既に共有し、MOの`Change_ResearchProjectDef.xml`で`Cocoa.label=Fruit tree sowing`・`baseCost=600`に再解釈している。**CocoaというDefNameはゲーム内表示ではなく、現状の研究参照自体は不具合ではない。** Coreの研究説明（ココア・チョコレート）のままでは果樹・養蚕の解禁説明として食い違うため、`Patches/Production/JapanizeMOAppleResearchText.xml`で`Cocoa.description`のみ実際の果樹栽培内容へ修正し、`Languages/Japanese/DefInjected/ResearchProjectDef/MO_FruitTreeSowing.xml`で`Cocoa.label=果樹栽培`と説明を加える。**研究コスト・前提`TreeSowing`・解禁する植物・桑の副産物`DankPyon_Silkworm`は変更しない。** この研究の元DefNameを丸ごと削除・交換・付け直す必要はない。なおCoreのカカオ樹への解禁が同一研究に残る問題は、Agriculture側のバニラ作物の時代選別と別に監査すること。

ユーザー指定により**画像は生成・置換しない**。同PatchでMOの既存リンゴ樹／生リンゴDefNameを維持して英語ラベル・説明のみ`Japanese apple tree`／`Japanese apples`（小型・比較的酸味がある和リンゴ）に改稿し、`Languages/Japanese/DefInjected/ThingDef/MO_Waringo.xml`に`和リンゴの木`／`和リンゴ`および説明を追加する。日本語翻訳Mod`Lucifel.MedievalOH.JPT`（Workshop 2665554648）は1.6原本で旧西洋リンゴの説明を持ち、`Cocoa`の果樹栽培訳を持たないため、`About/About.xml`の**任意`loadAfter`**にこのpackageIdを加え、Japanizationの修正訳を後順位とする。追加の必須依存にはしない。これは**文言の実装**であり、見た目が和リンゴに変わったことは意味しない。原本の樹木・収穫画像は西洋リンゴ相当のまま明記し、画像タスクはユーザー指示どおりスキップする。Agriculture PR #245のパイ・シードルの停止とPR #247の生育・収穫モデル、元`growDays=33`／`harvestYield=20`／腐敗15日／果実栄養0.05／価格1.1は変更しない。MO原本と和訳ZIPの対象XMLに静的照合できるが、英日表示の最終ロード優先順位・採集・研究・1.6/1.7実機の動作は未検証。

**2026-10-24 和リンゴの日本語・研究・果樹収穫、元RimWorld 1.6ネイティブ1回検証PASS（限定）:** Japanization [PR #26](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Medieval-Overhaul-Japanization/pull/26) は実ゲーム用`Tests/Waringo16`を追加し、[PR #27](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Medieval-Overhaul-Japanization/pull/27) main `c2128abadda4b724997bff1776268b21bb2e209f` で難易度補正付き実収穫計算に修正。Project手動限定 [PR #1014](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/pull/1014)／[PR #1015](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/pull/1015) main `6077381daef1d7bfd5faefe3448f61b33e41fe77` の`/amj moj-waringo-16`を初回実行し、難易度収量係数を考慮しない**固定収量10個のテスト前提**が実ゲーム早期収穫値17個に一致せず、[Actions #40084606772](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/40084606772) は **Pickle 0/1、Unity ERROR0、終了コード1、失敗理由 `Unexpected early loaded Apple YieldNow=17`** だった。これは和リンゴ実装の不一致ではなく検証用期待値の設計欠陥。Japanization PR #27でゲーム難易度の `cropYieldFactor` と最終ロードされた収穫下限を用いる式に修正し、同じ手動コマンドを**影響箇所に限り1回再実行**。[Actions #40085164460](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/40085164460) **SUCCESS**、元ライセンス付きLinux RimWorld `1.6.4871 rev598`、実際のMO・VEF・SYR・Environment `93c0ac45603b6d9d04d83edf8b404a05ab1aec34`・Agriculture `fce386f9b2c131bfb336d8508d0aa00ee85dae3f`・Scenarios `cd333acd463e44f1fec5099259f3622dc9946107`・Waterworks `bc7d755fd89b23dd7b57151655a81ba8af6868db`・Ironmaking `4e89419c3acae06031ba2d50fd592092916ec419`・Japanization `c2128abadda4b724997bff1776268b21bb2e209f` を隔離一時クローンで実ロード。**Pickle 1/1（flaky0、失敗0、skip0、attempt1）、Unity ERROR0、game exit0、timesout=false、`AMJ_MOJ_WARINGO16_OK`マーカー1件、`native_pass=true`。** 結果artifact `moj-waringo16-40085164460`（ID `12556523746`、SHA256 `8c77fb8b27d6a35c51d6fc6daf14c05bedac5a03cfee11f2aa7a623bae76db32`）、元ゲームのEXE SHA256 `0bfe51325720c950b4ad75ce7c3b65595fd7e939908520ec33600919919327a8`。2つの既知MO/SYR MP3 FMOD障害対策は**隔離コピー内でのみWAV化**し、本来のMO/SYR音声・ライセンスゲーム・作者のセーブを変更していない。元音声状態のERROR0を証明したわけではない。

**このPASSが実際に保証する範囲：** JavaScript/静的XMLではなく、**日本語（`Japanese (日本語)`）1.6ゲームのロード済みDef**で「和リンゴの木」「和リンゴ」・説明の小型／酸味表記、「果樹栽培」のラベル・養蚕説明、リンゴ／桑が`Cocoa`を研究前提として保持、蚕Def存在、リンゴの`growDays33`／`harvestYield20`／収穫後成長0.30／果実出力一致を確認。現物の樹木`Plant`を一時マップに生成し、Growth0.66で`HarvestableNow`と`YieldNow`の実値を難易度係数込みで照合し、`PlantCollected`後も枯死せずGrowth0.30に戻り採集不可になること、Growth1.0で満量計算になることを確認した。**実際の季節を通じた栽培・NPC作業による収穫／失敗、ゲーム画面で文字が正しく描画されるか、英語環境のロード、任意MO日本語翻訳併用時の表示優先、旧セーブ、他の未監査AMJ/MOコンテンツ、1.7は未検証**。この1ケースのPASSをMod一式リリースREADYや史実数値バランス承認と混同しない。Agriculture `fce386f`から最新ソース`10dc6ee40036eb3e473815a375454db017000015`への差は設計書・和リンゴ監査文書のみで実ゲームXMLには変更がないため、**和リンゴの生産スライスでは現行ソースも一致**。作者指定の画像作業は省略し、PNGの変更・画像評価・Steam公開・追加のネイティブ再実行は行わない。

#### Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） / MO日本化レイヤー

旧 `Japan Only` 方針は置き換え、正式名を **`Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）`** とする。

本Modは**Medieval OverhaulとAMJの全世界構成Modを必須前提とする、MO Patch + MO Retextureの公式AMJ一式統合レイヤー**である。単に西洋要素を削除するのではなく、MOが持つ中世の素材・加工段階・設備・生産システムを可能な限り再利用しながら、研究進行・名称/説明・Recipe/素材接続・表示資産を古代～中世日本として一貫するよう再構成する。

**2026-10-23 グリフォン幻想動物の通常入手経路遮断（MO 1.6.2.2）：** Agricultureがグリフォンベリーの栽培・料理・醸造・既存拠点戦利品の経路を整理した後、MO Japanizationはそれに付随するMO幻想動物の発生と供給を担当する。`Patches/Production/DisableGriffonOrdinaryAcquisition.xml`で、`DankPyon_GriffonPasses`の`baseChance`を0にしストーリーテラーからの通常ランダム発生を停止、グリフォンのAnimalFighter/AnimalExoticという専用`ThingDef.tradeTags`を空にして一般動物商人の供給を遮断する。無精卵・有精卵・グリフォン革の`tradeability=None`で通常商人の取扱いも停止する。**IncidentDef／ThingDef／PawnKindDef／卵・革・孵化・既存セーブの定義は削除しない**。既存の個体・卵・商人の在庫や外部Modの直接生成、特別なイベント実行、デバッグSpawnは禁止しない。`DankPyon_TreeGriffonBerry`は専用研究として不要だが、RimWorld 1.6 `MainTabWindow_Research.VisibleResearchProjects`は難易度`hideWhen`でフィルタするだけで**常時非表示の安全なXMLスイッチが存在しない**。研究Def削除や場外座標送り、誤った難易度条件設定は互換・UX上採用せず、研究ツリー再構築時の適切な表示経路の実装までDefと表示を暫定維持する。専用研究の残存を完成・全面除外と称さない。完成した薬物系MO野生薬草4種は監査保留を維持。XMLとMO実定義の静的照合は実施、実ゲーム1.6／1.7ロード・生成・UI／既存セーブの最終検証は未実施。

**2026-10-23 MO繊維転用の段階的実装（栽培→青苧→麻布）：** 日本の対象時代の代表的な植物繊維として採用済みの苧麻（カラムシ）をMO既存の`DankPyon_Plant_Flax`で再現する。Japanizationの`Patches/Production/JapanizeMORamieTextile.xml`が植物・`DankPyon_RawFlax`・`DankPyon_Linen`・麻布の製作Bill2種を既存DefNameのまま改称し、植物の播種解禁を`DankPyon_IntermediateAgriculture`から`DankPyon_TextileSpinning`へ移す。日本語の採用済み名称は`カラムシ／青苧／麻布／苧績み・麻布加工`。工業式`DankPyon_ClothSpinner`のみ新規建築メニューから外し、**MOの`clothChain` ON：原料→紡績Bill→布／OFF：収穫時に直接布**の経路は維持する。Agricultureは`Patches/MO_FibreCropPurpose.xml`により植物を`purpose=Misc`、収穫原料を`Textiles`に分類変更する（MO任意）。MO資源や設備、保存参照、研究Defや数値、一般的なProcessor Frameworkは削除しない。

**本段階の未完了：** MO亜麻植物の既存画像はカラムシの葉形と異なる。西洋の回転式`DankPyon_SpinningWheel`の造形も、中世日本の手作業設備として未採用のまま。画像差し替えは既存採用画像との監査と作者の画像採否が必要で、今回は一切画像生成・更新していない。カラムシは多年草だがMO植物は一年草型の収穫・再播種ループを流用しており、`growDays=7`、`harvestYield=18`などは歴史・バランス承認値ではない。Japanese DefInjectedでは決定済みの短い名称のみ追加し、新規の日本語歴史説明文は未承認のため追加しない。実ゲーム1.6/1.7の最終ロード、研究、栽培、紡績、交易/収納/旧セーブ、画像表示は未検証。責務・根拠・残課題は`Docs/Research/MedievalOverhaulJapanizationClothingTextileMapping.md`。

**2026-10-23 作者決定 — MO基盤の暫定活用と段階的独立:** AMJは最初からMOの素材加工／工房／研究／生産フレームワークを全部複製しない。**当面の統合ゲーム構成ではMOの適合する汎用機能を利用する**が、ゲーム内容・歴史考証・バランスはAMJの各正式Ownerが決める。Japanizationはその**MO依存の移行期アダプタ**であり、MOの西洋・幻想コンテンツを保存する権利を意味しない。日本固有の素材・作物・料理等は対応する独立AMJ Modが引き続き所有し、特に作物／料理の同一生産ループを分割しない。独立化は機能と原料→加工→完成品→研究・交易をひとまとまりとして、代替実装のプレイ上の価値が維持コストを上回る場合に実行する。**今はMOやJapanizationの必須依存・既存Def/Recipe/研究/保存参照を削除しない。** Japanizationを将来廃止すると決定したわけでもない。MO薬草4種（Mindwort/Poppy/Fleawort/Fly agaric）は専用薬品の供給源として現状維持・監査保留。MOに依存しないAMJ Modの既存単独動作は変更しない。正式な横断方針は[Project Architecture](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Architecture.md)に従う。

基本構成:
- MOなしで遊べる各AMJ Modは、従来どおり独立した主要ゲームループを持つ
- MOを利用する日本化構成: `RimWorld + Medieval Overhaul + AMJ世界構成の全Mod + Ancient & Medieval Japan - Medieval Overhaul Japanization`。**MO単独＋Japanization／一部AMJ ModだけのJapanization構成は非対応**
- **依存方向はJapanization → MOおよびAMJ全世界構成Modの一方向**。既存packageIdが確定したEnvironment、Grains（旧Crop Growth Balanceを含む）、Scenarios、Waterworks、Ironmakingは現時点からJapanizationの`About/About.xml`で必須。今後のCulture、Rice Cultivation、Factions、生活道具等の**独立Mod**はpackageId／本番提供が確定した段階で必須集合へ追加し、それまでは**AMJ一式として完成・公開可能とは扱わない**。各Mod自体はJapanizationなしで引き続き動作する。CCTO／CCTO for VPE等の独立汎用拡張、World Tech Level、DBH、VEなど外部Modはこの『全AMJ』に自動包含しない
- **2026-10-17作者決定の所有修正：** 山野採集（旧Wild Food Foraging）の採用済み12資源と採集機能は[Environment正本](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Environment/blob/main/Docs/ForagingIntegrationDesign-ja.md)へ統合する。Environmentはすでに必須のため、**独立WFF Modは今後のJapanization必須集合に加えない**。採集/農業の調整は全部入りAMJ構成の本来の要件であり、新Modを作る理由ではない。
- **World Tech Levelは、中世を越えるVanilla/他Mod要素をTech Levelで制限するための強い推奨Mod**とする。JapanizationはWorld Tech Levelの包括的制限機能を再実装せず、World Tech Level自体もJapanizationの必須依存にはしない
- MO本体のpackageId・既存Defを可能な限り維持し、MO互換Modとの接続を壊さずにPatchする

Patch側の責務:
- **MO全体の研究フローを、日本の古代～中世における技術発展とゲーム上の進行へ合わせて再構成する**
- 研究名・説明・前提関係・Tech Level・解禁設備/Recipeを必要に応じて変更する
- MOの素材加工段階（例: 鉱石→インゴット、原皮→革、原料→糸/布、穀物→粉等）は、日本側でも意味が成立するものを積極的に再利用する
- **必須Ironmakingを前提としたMO鉄資源供給調整を所有する。** Ironmaking自体はMO所有の鉄鉱床・Mine Shaftを変更しない。Japanization + Ironmakingの統合構成では、MOの地表鉄鉱床とMine Shaftの反復鉄鉱石Recipeを同じ供給系として監査し、砂鉄を主要ルート、MO鉄鉱石を副次ルートへ再調整する。鉄鉱石Defや経路を一律削除せず、出現頻度・鉱脈規模・Recipe出力/工数・研究位置等を必要に応じて調整する。正確な数値は実測で決める
- **JapanizationではIronmaking必須の日本製鉄ルートを前提としてMO鉄供給を調整する。** 従来の『IronmakingなしのJapanization』救済要件は廃止。独立したMO単独／MO＋Ironmakingの動作は、JapanizationでなくMOとIronmaking各所有者が担当する
- **MO商人の鉄材販売在庫を同じ総供給量として調整する。** 必須Ironmakingとの統合時に、MO所有TraderKindDefの鉄インゴット/鉄鉱石関連StockGeneratorを対象に、鉱床・Mine Shaftと合わせて供給を再調整する。輸入鉄材自体は国内製鉄開始以前の鍛冶や砂鉄の乏しい土地で必要なため残し、安価な大量・常時供給だけを抑える。具体的なStockGenerator数値・価格はテスト後に決定する
- **交易の範囲を鉄関連に限定する。** AMJ砂鉄の通常交易はIronmakingが所有し、Japanizationは日本化構成のMO既存商人在庫の追加調整だけを担当する。無関係なVanilla/外部Faction商人・Quest・世界技術の包括フィルタを行わない
- **MOゴーレム岩の鉄資源と幻想要素は別途一体監査する。** `DankPyon_GolemRock_Iron_MapGen`（鉱石450）と `DankPyon_GolemRock_Iron_Incident`（鉱石1000）は、独自GenStep・通常MapGeneratorへの追加Patch・GolemImpactorイベントと接続する。metalChain OFFで産出はIronIngotへ切り替わる。Japanizationの古代～中世日本史プロファイルでは、ゴーレム生成/イベントを保持する歴史的根拠がないため標準露出から切り離す候補として扱うが、PawnKind/Faction/Incident/生成経路・セーブ互換をまとめて確認するまで変更しない。Ironmaking単体でMOの当該経路には介入しない。詳細: `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`。
- **metalChain ONを砂鉄中心の参照バランス**とし、OFFはMOが鉄鉱床/Mine Shaftから鉄インゴットを直接出す互換プロファイルとして別検証する。ユーザーのOFF設定を黙ってONへ強制しない。MOの `ResourcesRaw` カテゴリから鉄原料が販売され得るため、個別インゴットStockGeneratorだけでなく最終在庫を検査する。Vanilla/外部Faction商人のSteel在庫はMO限定Patchで全世界制限しない。監査・残課題は `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`。
- 日本の対象時代・文化に合わないMO要素は、単純削除だけでなく、同等のゲーム上の役割を保てる場合は名称・説明・Recipe・研究位置・外観を日本向けへ置換する
- Mithril等、日本の歴史環境として扱わない幻想的・西洋的な進行経路は、他の進行を壊さないことを確認したうえで通常進行から外す
- MO互換Modが参照する既存Defを不用意に削除せず、非表示化・研究経路変更・Patchによる意味の置換を優先する。**Straw製造では上流`DankPyon_StrawProcess`を消さず、両乾燥ラックの使用可能プロセスからだけ除外**して既存参照を保存する
- MOのPawnKind / FactionDefが西欧装備・称号・紋章等を直接要求する場合は、**Japanization側でMO所有の装備表・表示を同時にPatchし、日本化後に西欧装備がNPC生成から再流入しないようにする**。ただし新しい日本史Factionの社会構造・集落・専用機能はAMJ Factionsの責務とする

Retexture側の責務:
- MO本体が所有する武器・防具・設備・建築等について、**ゲーム上の役割が日本の器物へ無理なく対応する場合は既存Defを維持したまま日本向けテクスチャへ差し替える**
- 武器・防具は、性能・Recipe・戦闘上の役割を変える必要がないものを原則としてリテクスチャ + 名称/説明Patchで日本化し、同等品のThingDefを重複追加しない
- 形だけ差し替えると実際の機能や歴史的意味と矛盾する対象は、リテクスチャだけで別物に見せかけず、Patch内容または所有責務を再検討する
- **MO所有資産のAMJ日本化リテクスチャはJapanizationへ集約**し、Grains等の各AMJ Modから同じMO texPathを競合上書きしない
- AMJ独自Defの画像は引き続き、そのDefを所有するAMJ Modが所有する

DBH for Medieval公式互換:
- **Dubs Bad Hygieneおよび `DBH for Medieval`（`eldersign.dbhformedieval`）をJapanizationの公式互換対象**とする。DBH / DBH for Medievalはハード依存にはしない
- 2026-10-07の添付Def監査では、DBH for Medievalが手動ポンプ、簡易浴槽、簡易トイレ、洗浄用具、湯沸かし、簡易浄水器、灌漑水路/水門等と独自研究を追加し、MO存在時にはSteel→`DankPyon_IronIngot`、ComponentIndustrial→`DankPyon_ComponentBasic`等の素材置換やMO風車研究との接続を行うことを確認した
- Japanization導入時は、DBH for Medievalの各設備を**実装機構まで含めて個別監査**する。中世ラベルを理由に一括保持しない。現行監査では、PrimitiveWell / ExcretionPit / Kettle / WashingKit / wooden 湯槽 / DBH灌漑を主要な保持候補とし、piston式ManualPump・WindPump・下水直結SimpleToilet・連続式FilterDeviceは標準歴史プロファイルから外す。DBH for MedievalのC#機能自体をJapanizationで再実装しない
- DBH for Medievalの `ES_IrrigationCanal` / `ES_SluiceGate` はDBH PipeNet / Sprinkler系であり、Waterworksの自然水面から直接取水する開渠とは**機能上別系統**として共存させる。現行Waterworks v1にはこのためのAdapterを要求しない。実際の消費者が必要性を示した場合だけ将来の任意Adapterを検討する
- Hot Springs併用時の入浴・給湯接続は、Hot Springs / Waterworksが所有する機能を尊重し、JapanizationはDBH側研究・既存設備の日本化と競合解決を担当する。詳細正本は `Docs/Research/MedievalOverhaulJapanizationDBHForMedievalMapping.md`

責務に含めないもの:
- 砂鉄供給・新しい日本製鉄ゲームループ・砂鉄の通常交易 → Ironmaking。MO所有の鉄鉱床・Mine Shaft・MO鉄材商人在庫を日本化構成で再調整する互換責務はJapanization側
- 日本の気候・地形・植生 → Japanese Environment
- 新しい日本史Faction・社会構造・集落機能の追加 → AMJ Factions。MO既存Faction / PawnKindのJapanizationと装備整合はJapanization側
- 日本固有イベント → AMJ Events
- Backstory／特性／一般の文化的心情／嗜好薬物の再構成 → 統合AMJ Culture（独立Backstory Modの既定計画は廃止）
- Grains / Rice Cultivation / Waterworks / Hot Springs / 発酵 / 酒造 / 保存等の独立ゲームループそのもの
- 外部Mod全般を日本要素だけに選別する汎用フィルタ

Japanizationは**「AMJ一式が存在する世界のMOを中世日本へ変換する層」**であって、新しいCoreではない。AMJ各Modの独立性を維持し、**Japanization側だけが全AMJ世界構成を必須依存**にする。MO単独の日本化を成立させるという旧方針を撤回する。

### 互換Patchの二層所有

Japanizationは「MOに関係するPatchをすべて集約するMod」ではない。

- **Standalone AMJ Mod ↔ MO の通常互換**は、そのStandalone Modが所有する。Japanizationなしの `MO + Grains`、`MO + Ironmaking` 等を壊さない。
- **JapanizationがMO自体を再構成した結果として必要になる追加調整**はJapanizationが所有する。

判断基準は「Patch対象がMO Defか」ではなく、**JapanizationなしのMO環境でもそのPatchが必要か**で決める。

詳細な所有・テストマトリクスは
`Docs/Research/MedievalOverhaulJapanizationIntegrationMatrix.md` を正本とする。

### MO再利用の粒度

MO連携は「MOの建物/研究を残すか消すか」というMod単位・研究単位の二択ではなく、**Def / Recipe / Process単位まで分解して再利用する**。

確定方針:
- MOのC# / Processor Framework / WorkTable等の基盤が有用でも、そこに同梱された全Recipe/Processを残す理由にはしない
- 一つの設備が複数工程を持つ場合、史実・ゲーム上の役割が成立する工程だけを残し、他は通常進行から切る
- 互換性のため上流Defは可能な限り残し、削除より研究経路・表示・Process露出のPatchを優先する
- 「実装済みだから使う」ではなく、**AMJでその工程が必要か**を先に判定する
- 各独立AMJ Modが所有するゲームループを、MO設備再利用を理由にJapanizationへ吸収しない

現時点の代表例:
- **Drying Rack:** 食品などの汎用乾燥機構として再利用。ただし**野草Hayを穀物藁Strawへ『乾燥だけで変える』工程は不採用**。Grainsの既存MO併用脱穀副産物`DankPyon_Straw`を藁供給源とし、`Patches/Production/DisableHayToStraw.xml`で小型・大型乾燥ラックの`DankPyon_StrawProcess`参照のみ除去する。ProcessDef自体と他の肉類等の乾燥工程は消さず、既存セーブで進行中のProcessor状態とTrading／既存配置物は1.6実機未検証。旧MO単独へのStraw供給保障はJapanizationの責務ではない
  **屋根付き乾燥台の小規模改善（2026-10-21、1.6実機未検証）:** `Patches/Production/RoofedDryingRacks.xml` により、既存の小型・大型 `DankPyon_DryingRack_*` の屋根設置禁止と `PlaceWorker_NotUnderRoof` を解除する。加工基盤はProcessor Frameworkのまま維持し、MO-ownedの干し肉3系統および魚Defが存在する場合の干し魚 `ProcessDef` に限って `sunFactor=0.85~1.0`、`windFactor=0.9~1.1` を適用する（上流は `0.5~1.0` と `0.75~1.25`）。PFの屋根判定は日照・風の両方を低下させるため、全面屋根下で倍率が0.375になる旧状態を約0.765に改善し、露天との差は残す。加工日数2.5日・歩留まり・容量・雨雪係数・研究・ProcessDefのIDと保存状態・`DankPyon_StrawProcess`の既存除外は変更しない。完全密閉室と軒下はPF標準の`RoofCoverage`だけでは区別できず、湿度・通風の独自再現は本変更に含めない。

  **長雨による加工失敗（2026-10-21、実ゲーム未検証）:** `Patches/Production/RainDamageDryingRacks.xml` で小型・大型乾燥台へ `CompDryingRainDamage` を追加し、PF既存の `activeProcesses[].ruinedPercent` を雨量×非屋根被覆率に応じて加算する。1.6のRimWorld本体とPFを参照する `Source/AMJ.MOJ.Drying/` のC#だけを追加し、`1.6/Assemblies/AncientMedievalJapanMOJDrying.dll` の実バイナリが存在しなければ動作しない（XMLだけを配布しない）。雨量1・屋根なしで累計2ゲーム日相当の雨にさらされると失敗率100%に達する仮値。雨量0なら加算なし、屋根で完全保護、部分屋根なら露出率に応じて加算する。雪はPFがRainRateを上げるため、本機構の雨損傷として重複計上しない。加工完了後・失敗済みのバッチ、保存済み `DankPyon_StrawProcess` は対象外。晴天による損傷回復は行わない。既存PFの失敗・回収UI・セーブを再利用し、独自ThingOwner・Bill・Job・品質ランクは作らない。PF本体・MO ProcessDef・加工日数・歩留まり・研究・他設備は変更しない。既存セーブへの追加CompとMO/PF実バイナリ、ロードDef、実プレイでの雨量・屋根・完成回収は1.6実機で未検証。
- **Millstone:** Bill式WorkTableとしてGrains等との任意接続に向く
- **Watermill:** 水力と穀物製粉は維持候補だが、MO同梱の2倍製材Processは標準から外す
- **Smoker:** PF機構は独自性があるが、日本の標準的な古代～中世保存技術としての根拠が弱いため標準非表示
- **Oil lighting:** 古代からの油灯を基礎として再利用
- **Andon / Candle:** 行灯は中世後期、蝋燭生産も後期枝として扱い、江戸で一般化した形を全時代の標準にはしない
- **Carrier Birds / Tar / Carpet Making:** AMJ標準進行から外し、上流Def互換だけ保持
- **Crossbow branch:** handheld Crossbow→`弩`、Heavy Crossbow→`強弩`、Scorpio→小型の設置`弩`を保持し、2x2・射程45のBallistaは重複する大型第2Tierとして標準非表示。Trebuchet / Repeater Ballistaも標準非表示

この原則により、MOを「大規模な前提コンテンツ一式」として受動的に受け入れるのではなく、**有用な中世ゲーム基盤を細粒度で再利用する層**として扱う。

### MO一般衣服とPawnKind

Japanizationは新しい和服カタログを追加するのではなく、**MO所有の一般衣服DefとMO PawnKindの西欧前提を、日本側の最小構成へ組み替える**。

現時点の主要キャリア:
- `DankPyon_Apparel_Sackcloth -> 小袖`
- `DankPyon_Apparel_Trousers -> 袴`
- `DankPyon_Footwear_BootsLeather -> 草鞋`（素材・防御/保温挙動をPatchし、農民への必須装備にはしない）
- `DankPyon_Handwear_GlovesLeather -> 弽`（一般手袋ではなく弓兵装備へ用途変更）
- `DankPyon_Apparel_Quiver -> 箙`（弓以外の遠隔武器まで高速化しないよう効果を監査）

MO集落のPeasant/Guardが現在強制しているPadded Surcoat、Leather Tunic、Padded Chausses、革手袋/革ブーツ、WoolMegasloth/Troll leather等の素材指定は標準日本化構成から外す。目的は独立AMJ Clothingの代替ではなく、**MOが生成するNPC自身から西欧常装を再流入させないこと**である。

詳細: `Docs/Research/MedievalOverhaulJapanizationCommonClothingMapping.md`.

### MO火縄銃の機械Patch

`DankPyon_Handgonne` は現行MOで射程12.9・3連射の近距離burst武器なので、画像と名称だけを火縄銃へ変えてはならない。

初回バランステスト用Prototype A:
- single shot;
- damage 30;
- AP .35;
- range 28;
- warmup 2.25 s;
- cooldown 5.5 s;
- accuracy .75 / .78 / .60 / .35;
- upstreamの `ShootingAccuracyPawn +2` は除去。

これは本番値ではなく、War Bow / Crossbow / Heavy Crossbowとの自動比較用の開始点とする。MO Handgonneは弾薬消費システムを持たないため、初回Japanizationでは新規弾薬システムを追加せず射撃挙動だけをPatchする。


### 家具・建築とMO集落生成

家具・建築は、プレイヤーの建築メニューだけでなく **MOのStructureLayoutDef / SymbolDefによる集落・サイト生成**まで含めて日本化する。

確定方針:
- 生成で大量参照されるDefは、単純非表示にせず、同じDefを日本側の対応物へ再解釈するか、生成側を同時に差し替える
- `DankPyon_CastleWall` はKCSG SymbolDef経由で**8,565のレイアウトセル**から参照され、直接リンク込みでは8,568生成参照となるため削除対象ではない。高い日本式囲い塀（築地塀 / 練塀級）へ再解釈し、`石垣`とは呼ばない
- `DankPyon_TudorWall` は木骨＋Clayという機能を活かし、日本の土壁系へ再解釈する
- MOのRoyal家具は集落生成参照が多いため、椅子・dresser・Tudor bedを一括非表示にせず、厨子・棚・格式ある寝所・御座等の**実際の機能に合う日本側調度**へ個別対応する
- `DankPyon_RTrench` は単なる高pathCostの建築物であり、堀/空堀へ見せ替えない。標準非表示とし、防御土木は別責務とする
- MOのKilnは設備Def自体は再利用候補だが、現行のClay block→西洋装飾床群を残す理由にはしない。正当な陶磁/瓦等の所有ループがない限り、現行Processは標準から外す
- 日本式家具を新規Defで大量追加するのではなく、MO既存Defの正直な再解釈と既存和風家具Modの併用を優先する

詳細台帳: `Docs/Research/MedievalOverhaulJapanizationFurnitureArchitectureMapping.md`.


### 2.10 MOの研究フローを古代～中世日本史へ再構成する

Medieval Overhaulの研究順は西欧中世を主軸にしたゲーム的抽象化であり、Japanization導入時にはその順序を日本側の技術史へそのまま従属させない。**`Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）` がMO全体の研究フロー再構成を所有する。**

基本原則:
- AMJの対象は古代～中世であり、江戸・近世の完成形を標準研究Tierへ持ち込まない
- 「強い設備ほど後半」だけで並べず、日本での技術成立時期、必要な前提技術、素材加工、ゲーム上の導線を合わせて研究位置を決める
- MO既存の素材・加工段階・設備が日本でも意味を持つ場合はDefを維持して研究位置を変更し、不要な複製を作らない
- 西欧固有の研究名・前提関係は、日本側で同等の技術的意味が成立する場合に名称/説明と接続を置換する
- 日本側に対応する意味がなく、除去しても進行が成立する研究・解禁経路は非表示化/切断対象にできる
- World Tech LevelはIndustrial以降等を包括的に制限する外部層として扱い、Japanizationの研究再構成とは分担する

AMJ各独立Modは、自分が所有する機能の研究・解禁条件を引き続き所有する。Japanizationはそれらを吸収せず、MO併用時に必要な接続だけを提供する。たとえばIronmakingは日本製鉄そのものを所有し、JapanizationはMO鍛冶・金属加工研究との接続やMO側の不要/不適切な経路整理を担当する。Ironmakingは独自の「鉄器加工」研究を重複追加せず、既存鍛冶を前段階として初期製鉄から始めるため、JapanizationもMO側の鍛冶研究を接続点として利用する。Ironmaking併用時のMO鉄鉱床・Mine Shaft供給量の調整も、MO所有Def/Recipeを変更する互換処理なのでJapanizationの責務とする。

作物・農業についても、作物固有の性能値はGrains / Rice Cultivation等の所有Modで先に決め、Japanizationの研究Tierへ合わせるために性能を逆算しない。研究位置を決める際は、日本での利用・栽培時代、栽培技術、収穫後加工、MO既存設備との接続、ゲーム上の進行導線を合わせて判断する。

**2026-10-19 統合訂正:** 旧Japanizationレンズ豆スキル2パッチは**Grainsの任意MO互換パッチへ移管・削除済み**。同じGrainsが旧Crop Growth Balanceのバニラ6＋MO7作物のgrowDaysも所有する。Japanizationは作物のスキル・生育日数を二重Patchせず、日本化研究・生産・表示だけを調整する。GrainsなしでJapanizationを利用する構成は引き続き非対応。収穫量・栽培技能の追加均衡はGrainsがまとめて検討する。


---


### 実装対象研究グラフとPatchマニフェスト

67ノードの初回監査を経て、プレイヤーへ見せる最終候補研究構造は
`Docs/Research/MedievalOverhaulJapanizationTargetResearchGraph.md`
を正本とする。

機械可読版:
- `Docs/Research/Data/MedievalOverhaulJapanizationResearchGraph.csv`
- `Docs/Research/Data/MedievalOverhaulJapanizationDBHResearchOverlay.csv`

専用Japanizationリポジトリ作成後の実装単位・順序は
`Docs/Research/MedievalOverhaulJapanizationProductionPatchManifest.md`
を引き継ぐ。

本リポジトリをJapanizationの実装正本とし、研究グラフ・判断台帳・Patch・Retexture・テストをここで管理する。
