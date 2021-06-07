dan  callsmusic . USER olarak callmusic  ithalat  istemcisi  
dan  pyrogram  ithalat  Client , filtreler
dan  pyrogram . türleri  import  Message , InlineKeyboardButton , InlineKeyboardMarkup
dan  pyrogram . Hatalar  UserAlreadyParticipant'ı içe  aktarıyor
dan  yardımcıları . dekoratörler  ithalat  hataları , yetkili_kullanıcılar_yalnızca

@ Müşteri . on_message ( filtreler . grup  ve  filtreler . komut ([ "katil" ]))
@ yetkili_users_only
@ hatalar
zaman uyumsuz  def  addchannel ( istemci , mesaj ):
    chid  =  mesaj . sohbet . İD
    dene :
        davet bağlantısı  =  müşteri bekliyor  . export_chat_invite_link ( chid )
    hariç :
         mesaj bekliyoruz . cevap_metni (
            "<b>Önce Anonim Gönder seçeneği dışındaki tüm izinler için beninun belediyesi olarak ekle</b>" ,
        )
        dönüş

    dene :
        Kullanıcı  =  bekliyoruz  USER . get_me ()
    hariç :
        kullanıcı . first_name  =   "HirasetAsistan" 

    dene :
         KULLANICIYI bekleyin . join_chat ( davet bağlantısı )
         KULLANICIYI bekleyin . send_message ( mesaj . sohbet . id , "İstediğiniz gibi buraya katıldım" )
     UserAlreadyParticipant hariç :
         mesaj bekliyoruz . cevap_metni (
            "<b>Asistanınız zaten sohbetinizde</b>" ,
        )
        geçmek
     e olarak İstisna  hariç : 
        yazdır ( e )
         mesaj bekliyoruz . cevap_metni (
            f"<b🛑 Taşan Bekleme 🛑 \n kullanıcı { user . first_name } userbot için yoğun katılımda ekibine katılamadı!
            " \n \n Veya ekibine el ile @SesmusicAsistan ekleyin ve yeniden deneyin</b>" ,
        )
        dönüş
     mesaj bekliyoruz . cevap_metni (
            "<b>asistan sohbetinize katıldınız 😎</b>" ,
        )
    
@ KULLANICI . on_message ( filtreler . grup  ve  filtreler . komut ([ "ayril" ]))
zaman uyumsuz  def  rem ( KULLANICI , mesaj ):
    dene :
         KULLANICIYI bekleyin . Leave_chat ( mesaj . sohbet . id )
    hariç :  
         mesaj bekliyoruz . cevap_metni (
            f"<b>Kullanıcı gruplarından ayrılamadı! Floodwaits olabilir."
            " \n \n Ya da beni manuel olarak grupuza Al veya kov 🤣.</b>" ,
        )
        dönüş
 