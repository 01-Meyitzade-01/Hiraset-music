
 işletim sistemini içe aktar
içe aktarma  istekleri
 aiohttp'yi içe aktar
 youtube_dl'yi içe aktar

dan  pyrogram  ithalat  filtreleri , Müşteri
dan  youtube_search  ithalat  YoutubeSearch

def  time_to_seconds ( zaman ):
    stringt  =  str ( zaman )
    Dönüş  toplamı ( int ( x ) *  60  **  i  için  i , x  in  numaralandırmak ( ters ( Stringt . bölme ( ':' ))))


@ Müşteri . ON_MESSAGE ( filtreler . komutu ( 'ytindir' ) ve  ~ filtreler . Özel  ve  ~ filtreler . kanalı )
def  ytindir ( istemci , mesaj ):

    user_id  =  mesaj . from_user . İD 
    user_name  =  mesaj . from_user . İsim 
    rpk  =  "[" + kullanıcı_adı + "](tg://user?id=" + str ( user_id ) + ")"

    sorgu  =  ''
    için  i  içinde  mesajın . komut [ 1 :]:
        sorgu  +=  ' '  +  str ( ben )
    yazdır ( sorgu )
    m  =  mesaj . cevap ( '🔎 Şarkıyı arıyorum...' )
    ydl_opts  = { "biçim" : "bestaudio[ext=m4a]" }
    dene :
        sonuçlar  =  YoutubeArama ( sorgu , max_results = 1 ). to_dict ()
        link  =  f"https://youtube.com { sonuçlar [ 0 ][ 'url_suffix' ] } "
        #print(sonuçlar)
        başlık  =  sonuçlar [ 0 ][ "başlık" ][: 40 ]       
        küçük resim  =  sonuçlar [ 0 ][ "küçük resimler" ][ 0 ]
        thumb_name  =  f'thumb { başlık } .jpg'
        başparmak  =  istekler . get ( küçük resim , allow_redirects = True )
        aç ( thumb_name , 'wb' ). yazmak ( başparmak . içerik )


        süre  =  sonuçlar [ 0 ][ "süre" ]
        url_suffix  =  sonuçlar [ 0 ][ "url_suffix" ]
        görüntüleme  =  sonuçlar [ 0 ][ "görüntüleme" ]

     e olarak İstisna  hariç : 
        m . düzenle (
            "❌ Hiçbir Şey Bulamadım. \n \n Başka bir Kelime dene veya düzgün hecele."
        )
        yazdır ( str ( e ))
        dönüş
    m . edit ( "Youtube üzerinden indirilerek yapıldı..." )
    dene :
        ile  youtube_dl . YoutubeDL ( ydl_opts ) olarak  YDL :
            info_dict  =  ydl . Extract_info ( bağlantı , indirme = Yanlış )
            audio_file  =  ydl . hazırla_dosyaadı ( info_dict )
            ydl . process_info ( info_dict )
        rep  =  '**🎵 hiraset tarafından yüklendi**'
        secmul , dur , dur_arr  =  1 , 0 , süre . böl ( ':' )
        için  I  içinde  aralığı ( len ( dur_arr ) - 1 , - 1 , - 1 ):
            dur  += ( int ( dur_arr [ ben ]) *  secmul )
            secmul  *=  60
        mesaj . answer_audio ( audio_file , caption = rep , thumb = thumb_name , parse_mode = 'md' , başlık = başlık , süre = dur )
        m . sil ()
     e olarak İstisna  hariç : 
        m . düzenle ( '❌ Hata' )
        yazdır ( e )

    dene :
        os . kaldır ( audio_file )
        os . kaldır ( thumb_name )
     e olarak İstisna  hariç : 
        yazdır ( e )