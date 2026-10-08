> **Authority:** This repository is now the authoritative owner of Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）. Project-level copies are migration history only and must not evolve independently.

# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） — Design

**Status:** dedicated owner repository active; initial implementation planning (Project pre-split history migrated here).

The concept is defined, but there is no dedicated owner repository yet. Project owns the evolving pre-split design.

#### Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） / MO日本化レイヤー

旧 `Japan Only` 方針は置き換え、正式名を **`Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）`** とする。

本Modは**Medieval Overhaulを必須前提とする、MO Patch + MO Retextureの公式AMJ統合レイヤー**である。単に西洋要素を削除するのではなく、MOが持つ中世の素材・加工段階・設備・生産システムを可能な限り再利用しながら、研究進行・名称/説明・Recipe/素材接続・表示資産を古代～中世日本として一貫するよう再構成する。

基本構成:
- MOなしで遊べる各AMJ Modは、従来どおり独立した主要ゲームループを持つ
- MOを利用する日本化構成: `RimWorld + Medieval Overhaul + Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） + 任意のAMJ Mod`
- JapanizationはMOを必須依存とするが、Grains / Rice Cultivation / Waterworks / Hot Springs / Ironmaking等からJapanizationを必須依存にはしない
- **World Tech Levelは、中世を越えるVanilla/他Mod要素をTech Levelで制限するための強い推奨Mod**とする。JapanizationはWorld Tech Levelの包括的制限機能を再実装せず、World Tech Level自体もJapanizationの必須依存にはしない
- MO本体のpackageId・既存Defを可能な限り維持し、MO互換Modとの接続を壊さずにPatchする

Patch側の責務:
- **MO全体の研究フローを、日本の古代～中世における技術発展とゲーム上の進行へ合わせて再構成する**
- 研究名・説明・前提関係・Tech Level・解禁設備/Recipeを必要に応じて変更する
- MOの素材加工段階（例: 鉱石→インゴット、原皮→革、原料→糸/布、穀物→粉等）は、日本側でも意味が成立するものを積極的に再利用する
- **Ironmaking併用時のMO鉄資源供給調整を所有する。** Ironmaking自体はMO所有の鉄鉱床・Mine Shaftを変更しない。Japanization + Ironmakingの統合構成では、MOの地表鉄鉱床とMine Shaftの反復鉄鉱石Recipeを同じ供給系として監査し、砂鉄を主要ルート、MO鉄鉱石を副次ルートへ再調整する。鉄鉱石Defや経路を一律削除せず、出現頻度・鉱脈規模・Recipe出力/工数・研究位置等を必要に応じて調整する。正確な数値は実測で決める
- **Ironmaking未導入時はMO鉄資源経路を実用可能な状態に保つ。** Japanization単独で鉄供給を壊さず、Ironmakingがある場合だけ日本式砂鉄ルートとの全体バランスを取る
- **MO商人の鉄材販売在庫を同じ総供給量として調整する。** Ironmaking併用時のみ、MO所有TraderKindDefの鉄インゴット/鉄鉱石関連StockGeneratorを対象に、鉱床・Mine Shaftと合わせて供給を再調整する。輸入鉄材自体は国内製鉄開始以前の鍛冶や砂鉄の乏しい土地で必要なため残し、安価な大量・常時供給だけを抑える。具体的なStockGenerator数値・価格はテスト後に決定する
- **交易の範囲を鉄関連に限定する。** AMJ砂鉄の通常交易はIronmakingが所有し、Japanizationは日本化構成のMO既存商人在庫の追加調整だけを担当する。無関係なVanilla/外部Faction商人・Quest・世界技術の包括フィルタを行わない
- **metalChain ONを砂鉄中心の参照バランス**とし、OFFはMOが鉄鉱床/Mine Shaftから鉄インゴットを直接出す互換プロファイルとして別検証する。ユーザーのOFF設定を黙ってONへ強制しない。MOの `ResourcesRaw` カテゴリから鉄原料が販売され得るため、個別インゴットStockGeneratorだけでなく最終在庫を検査する。Vanilla/外部Faction商人のSteel在庫はMO限定Patchで全世界制限しない。監査・残課題は `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`。
- 日本の対象時代・文化に合わないMO要素は、単純削除だけでなく、同等のゲーム上の役割を保てる場合は名称・説明・Recipe・研究位置・外観を日本向けへ置換する
- Mithril等、日本の歴史環境として扱わない幻想的・西洋的な進行経路は、他の進行を壊さないことを確認したうえで通常進行から外す
- MO互換Modが参照する既存Defを不用意に削除せず、非表示化・研究経路変更・Patchによる意味の置換を優先する
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
- Backstory追加 → AMJ Backgrounds
- Grains / Rice Cultivation / Waterworks / Hot Springs / 発酵 / 酒造 / 保存等の独立ゲームループそのもの
- 外部Mod全般を日本要素だけに選別する汎用フィルタ

Japanizationは**「MOを中世日本へ変換する層」**であって、新しいCoreではない。AMJ各Modの独立性を維持したまま、MOを採用する構成だけを深く統合する。

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
- **Drying Rack:** 汎用乾燥機構として強い再利用候補
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
