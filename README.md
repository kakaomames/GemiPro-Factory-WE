# GemiPro-Factory-WE
## 概要 / Overview
本プロジェクトは、Gemini programming隊（カカオマメ隊員 & 隊長）による、
APK解体・Web版変換のための全自動変換工廠です。

「動けば正義。壊れなければ問題ない。」をスローガンに、
GitHub Actionsの6時間枠とJava 21、最新のAPKEditorを活用して、
あらゆるAPKをWebで動作可能な形式（Web Edition）へと変換します。

## システム構成
- 司令塔: Vercel (APK Upload & GitHub Push)
- 重機: GitHub Actions (Java 21 / Python / APKEditor / Android.jar)
- 基地: Local Server (python -m http.server 8080)

## 自動生成される項目
以下のディレクトリおよびファイルは、Pythonスクリプト（scripts/decompile_engine.py）
によって実行時に自動的に生成・管理されます。
- apks/ : ターゲットAPKの保管場所
- tools/ : 最新JAR兵器の調達場所
- www/assets/ : 抽出されたリソース群
- www/index.html : metaタグ満載のメインUI
- result.json : 変換ステータス報告書

## 利用規約 / Disclaimer
1. 本ツールはリバースエンジニアリングの研究および学習を目的とした個人用ツールです。
2. 著作権はそれぞれの権利者に帰属します。
3. 使用によって生じたトラブルや損害について、開発者は一切の責任を負いません。
4. 全ては「自己責任」において実行してください。
