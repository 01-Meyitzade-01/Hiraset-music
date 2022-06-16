{
  " name " : " Myt Müzik Botu " ,
  " description " : " Telegram'ın Grup Sesli Sohbetinde şarkı çalmak için Açık Kaynak bot. PyTgCalls tarafından desteklenmektedir. " ,
  " keywords " : [ " music " , " voice chat " , " telegram " ],
  " repo " : " https://github.com/01-Meyitzade-01/hiraset-music " ,
  " stack " : " inclusive " ,
  " env " : {
    " SESSION_NAME " : {
      " description " : " Pyrogram öğretmesi " ,
      " necessary " : true
    },
    " BOT_TOKEN " : {
      " description " : " Bir bot belirteci @BotFather " ,
      " gerekli " : true
    },
    " BOT_NAME " : {
      " description " : " MusicPlayer Bot Adınız. " ,
      " necessary " : false ,
      " value " : " Myt Müzik "
    },
    " API_ID " : {
      " description " : " my.telegram.org/apps adresinden Uygulama Kimliği " ,
      " necessary " : true
    },
    " API_HASH " : {
      " description " : " my.telegram.org/apps adresinden uygulama karması " ,
      " necessary " : true
    },
    " SUDO_USERS " : {
      " description " : " Her yerde yönetici olarak sayılan kullanıcı kimliklerinin listesi. " ,
      " necessary " : true
    },
    " DURATION_LIMIT " : {
      " description " : " için en fazla ses tahmini İndirmeler(dakikalar). " ,
      " necessary " : true ,
      " value " : " 50 "
    }
  }
}
