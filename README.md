# Minecraft with Python (이하 Mython)  
* SNUCODE PROJECT

## MYTHON 설치 방법
> ### https://drive.google.com/file/d/1czDUJYr93kmCnpa-PK7bf4GXyy7vz9wp/view?usp=sharing Chapter 1 참조
>
> * Python 설치 (Python 3.xx 버전) https://www.python.org/downloads/  
> ※ 주의 Python 설치시 Add Python 3.x to PATH 항목을 체크 해야함 <p/>
> * Java 설치 https://www.java.com/ko/ <p/>
> * Minecraft 설치 (Minecraft 1.11.2 버전 필요) https://minecraft.net/ko-kr/download/?ref=bm <p/>
> * Python API 설치 및 서버 구동  
>   Windows : https://sourceforge.net/projects/program-with-minecraft/  
>   Mac OS : https://sourceforge.net/projects/program-with-minecraft-mac/
> 
>  1. 각 os에 맞게 Minecraft Tools.zip 파일을 다운받고 압축을 푼다.
>  2. Minecraft Tools 폴더 안에 있는 Install_API.bat 파일을 실행시켜 API를 설치한다.

## MYTHON 실행
> * Minecraft Tools 폴더 안에 있는 Start_Server 바로가기를 실행 시켜 서버를 연다.   
> ※ 주의 서버 창을 닫으면 안된다. 서버 창이 열려 있어야 서버에 접속 할 수 있다. <p/>
> * 다운 받은 Minecraft 를 서버 버전에 맞게 실행시킨다.  
> ※ 서버 버전은 서버 창의 Starting minecraft server version x.x.x 에서 확인 할 수 있다. 
> * Minecraft 가 실행 되면 Multiplayer 로 들어가 Add Server 를 누르고 Server Address 를 'localhost' 라고 한뒤 Done을 눌러 서버에 접속한다. <p/>
> * 그럼 이제 Python 에디터를 열어 맘껏 프로그램을 만들면 된다! <p/>
> * 예제 프로그램
>    ```python
>    from mcpi.minecraft import Minecraft
>    mc = Minecraft.create()
>    mc.postToChat("Hello world")
>    ```
## 참고 문헌
> * https://nostarch.com/programwithminecraft   
> * https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi/5
> * http://www.stuffaboutcode.com/p/minecraft.html
> * https://minecraft-ko.gamepedia.com/Server.properties

## Mython Installer (beta)
> * https://www.dropbox.com/s/onl6zxms0ddtnuk/Mython_Installer.zip?dl=1
