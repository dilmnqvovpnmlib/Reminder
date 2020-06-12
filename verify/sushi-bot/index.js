// -----------------------------------------------------------------------------
// モジュールのインポート
const server = require("express")();
const line = require("@line/bot-sdk"); // Messaging APIのSDKをインポート

// -----------------------------------------------------------------------------
// パラメータ設定
const line_config = {
  channelAccessToken: process.env.LINE_ACCESS_TOKEN, // 環境変数からアクセストークンをセットしています
  channelSecret: process.env.LINE_CHANNEL_SECRET, // 環境変数からChannel Secretをセットしています
};

// -----------------------------------------------------------------------------
// Webサーバー設定
server.listen(process.env.PORT || 3000);

const bot = new line.Client(line_config);
// -----------------------------------------------------------------------------
// ルーター設定
server.post("/bot/webhook", line.middleware(line_config), (req, res, next) => {
  res.sendStatus(200);
  console.log("Hello", req.body);
  // {
  //   2020-06-12T16:16:54.106134+00:00 app[web.1]: events: [
  //   2020-06-12T16:16:54.106134+00:00 app[web.1]: {
  //   2020-06-12T16:16:54.106135+00:00 app[web.1]: type: 'message',
  //   2020-06-12T16:16:54.106136+00:00 app[web.1]: replyToken: 'c3f1eff682a34a738f2963626c0d5055',
  //   2020-06-12T16:16:54.106136+00:00 app[web.1]: source: [Object],
  //   2020-06-12T16:16:54.106136+00:00 app[web.1]: timestamp: 1591978613334,
  //   2020-06-12T16:16:54.106137+00:00 app[web.1]: mode: 'active',
  //   2020-06-12T16:16:54.106137+00:00 app[web.1]: message: [Object]
  //   2020-06-12T16:16:54.106137+00:00 app[web.1]: }
  //   2020-06-12T16:16:54.106137+00:00 app[web.1]: ],
  //   2020-06-12T16:16:54.106138+00:00 app[web.1]: destination: 'U4a4b18ba58918e0a03dcc5e3c21bf5f4'
  //   2020-06-12T16:16:54.106138+00:00 app[web.1]: }
  // すべてのイベント処理のプロミスを格納する配列。
  let events_processed = [];

  // イベントオブジェクトを順次処理。
  req.body.events.forEach((event) => {
    console.log("event.message", event.message); // { type: 'text', id: '12133726520537', text: 'こんにちは' }
    // この処理の対象をイベントタイプがメッセージで、かつ、テキストタイプだった場合に限定。
    if (event.type == "message" && event.message.type == "text") {
      // ユーザーからのテキストメッセージが「こんにちは」だった場合のみ反応。
      if (event.message.text == "こんにちは") {
        // replyMessage()で返信し、そのプロミスをevents_processedに追加。
        events_processed.push(
          bot.replyMessage(event.replyToken, {
            type: "text",
            text: "Hello",
          })
        );
      }
    }
  });

  // すべてのイベント処理が終了したら何個のイベントが処理されたか出力。
  Promise.all(events_processed).then((response) => {
    console.log(`${response.length} event(s) processed.`);
  });
});
