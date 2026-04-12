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

5. # GemiPro-Factory-WE (English Edition)

## Overview
This project is an automated APK deconstruction and Web Edition conversion factory developed by the Gemini Programming Unit (Kakaomames & Captain).

Motto: "Functionality is Justice. As long as it works, there's no problem."

By leveraging GitHub Actions' 6-hour execution window, Java 21, and the latest APKEditor, this system converts APKs into web-compatible formats (Web Edition) automatically.

## System Architecture
- Commander: Vercel (Handles APK uploads and triggers GitHub pushes)
- Heavy Machinery: GitHub Actions (Environment: Java 21, Python, APKEditor, Android.jar)
- Base: Local Server (Runs via `python -m http.server 8080`)

## Automated Generation
The following directories and files are dynamically generated and managed by the Python supervisor (`scripts/decompile_engine.py`) during execution:
- apks/ : Storage for target APK files
- tools/ : Deployment area for the latest JAR tools (fetched via curl)
- www/assets/ : Extracted resources and assets
- www/index.html : Main UI with optimized meta tags
- result.json : Real-time conversion status report

## Disclaimer
1. This tool is for educational and research purposes regarding reverse engineering.
2. All copyrights for uploaded APKs and extracted data belong to their respective owners.
3. The developer is not responsible for any issues or damages caused by the use of this tool.
4. Use at your own risk. "If it works, it's justice."

