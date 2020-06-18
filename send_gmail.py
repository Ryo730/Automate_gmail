from smtplib import SMTP
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def sendGmailAttach(sub,text,filename,path):
    #送信元メールアドレスとgmailパスワード
    sender,password="cityleft21@gmail.com","smskfeamykvosgor"
    #送信先メールアドレス
    to='miyamoto073015@gmail.com'
    #メール件名
    sub=sub
    #メール本文
    body=text
    #Evernoteの記事参照
    #host,post="smtp.gmail.com",587

    ##メールヘッダ
    #ファイル添付用メソッド→attach()メソッドが使える
    msg=MIMEMultipart()
    msg['Subject']=sub
    msg['From']=sender
    msg['To']=to

    ##メール本文
    body=MIMEText(body)
    msg.attach(body)

    ##添付ファイルの設定
    #nameは添付ファイル名，pathは添付ファイルの位置を設定する
    #例→doi_flag.png,'/Users/miyamotoryo/Desktop/first-tutorial/flags.image/doi_flag.png'
    attach_file={'name':filename,'path':path}
    #よくわからん.→添付ファイルの端子の設定？？
    attachment=MIMEBase("image","png")

    ##ファイル開く
    #第一引数＝pathでファイル指定，第二引数＝modeの選択（読み取り専用，書き込み，etc）
    file=open(attach_file['path'],"rb+")
    #よくわからん
    attachment.set_payload(file.read())
    #ファイル閉じる
    file.close()
    encoders.encode_base64(attachment)
    #ヘッダーに文字追加？？
    attachment.add_header("Content-Disposition","attachment",filename=attach_file['name'])
    #送信メールの添付ファイルをattachmentに設定？？
    msg.attach(attachment)

    ##Gmailへ接続（SMTPサーバとして利用）
    #SMTPサーバに接続？？
    gmail=SMTP("smtp.gmail.com",587)
    #SMTP通信のコマンドを暗号化し，サーバアクセスの認証を通す
    gmail.starttls()
    #Gmailアカウントにメールアドレスとパスワードを入力してログイン
    gmail.login(sender,password)
    #msgをアカウントから送信
    gmail.send_message(msg)


##実行

if __name__=="__main__":
    print("件名を入力して下さい")
    sub=input()
    print("本文を入力して下さい")
    text=input()
    print("ファイル名を入力して下さい")
    filename=input()
    print("ファイルパスを入力して下さい")
    path=input()
    sendGmailAttach(sub,text,filename,path)
    print("メールが送信されました")