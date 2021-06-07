{
  " name " : " Hiraset Müzik Botu " ,
  " description " : " Telegram'ın Grup Sesli Sohbetinde şarkı çalmak için Açık Kaynak bot. PyTgCalls tarafından desteklenmektedir. " ,
  " anahtar kelimeler " : [ " müzik " , " sesli sohbet " , " telgraf " ],
  " depo " : " https://github.com/01-Meyitzade-01/hiraset-music " ,
  " yığın " : " kapsayıcı " ,
  " env " : {
    " OTURUM_NAME " : {
      " description " : " Pyrogram öğretmesi " ,
      " gerekli " : doğru
    },
    " BOT_TOKEN " : {
      " description " : " Bir bot belirteci @BotFather " ,
      " gerekli " : doğru
    },
    " BOT_NAME " : {
      " description " : " MusicPlayer Bot Adınız. " ,
      " gerekli " : yanlış ,
      " değer " : " hiraset müzik "
    },
    " API_ID " : {
      " description " : " my.telegram.org/apps adresinden Uygulama Kimliği " ,
      " gerekli " : doğru
    },
    " API_HASH " : {
      " description " : " my.telegram.org/apps adresinden uygulama karması " ,
      " gerekli " : doğru
    },
    " SUDO_USERS " : {
      " description " : " Her yerde yönetici olarak sayılan kullanıcı kimliklerinin listesi. " ,
      " gerekli " : doğru
    },
    " DURATION_LIMIT " : {
      " description " : " için en fazla ses tahmini İndirmeler(dakikalar). " ,
      " gerekli " : doğru ,
      " değer " : " 45 "
    }
  }
}