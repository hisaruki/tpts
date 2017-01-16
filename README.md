# Twitterの画像ファイルを整理するスクリプト

## 概要

ローカルに保存された(pbs.twimg.comから保存した)画像のパスを渡すと以下のことをします

1. 画像の元URLにアクセスしLast-ModifiedとContent-Lengthをチェック
2. ローカルファイルのサイズがContent-Lengthより小さい(:largeでない画像を保存していた)場合、画像を取得しなおして上書き保存
3. ローカルファイルのタイムスタンプをサーバーのLast-Modifiedに合わせる
4. ファイル名を*.ext-large.extにリネーム

## 今後の予定

largeじゃなくorigがある場合をチェックはorigを使うようにしたい