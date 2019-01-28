import socket
import sys

if __name__ == '__main__':
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建Socket连接（TCP）
   print('Socket Created')

   try:
       sock.bind(('127.0.0.1', 8001))  # 配置Socket，绑定IP地址和端口号
   except socket.error as e:
       print('Bind Failed...', e)
       sys.exit(0)

   sock.listen(5)  # 设置最大允许连接数，各连接和Server的通信遵循FIFO原则

   while True:  # 循环轮询Socket状态，等待访问
       conn, addr = sock.accept()
       try:
           conn.settimeout(10)  # 获得一个连接，然后开始循环处理这个连接发送的信息

           # 如果要同时处理多个连接，则下面的语句块应该用多线程来处理
           while True:
               data = conn.recv(1024)
               data = str(data, encoding="utf-8")
               print('Get value ' + data, end='\n\n')
               if not data:
                   print('Exit Server', end='\n\n')
                   break
               conn.sendall(b'OK')  # 返回数据
       except socket.timeout:  # 建立连接后，该连接在设定的时间内没有数据发来，就会引发超时
           print('Time out')

       conn.close()  # 当一个连接监听循环退出后，连接可以关掉
   sock.close()
