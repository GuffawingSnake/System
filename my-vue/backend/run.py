from app import create_app

app = create_app()

if __name__ == '__main__':
    print("启动Flask服务器...")
    print("监听地址: http://127.0.0.1:5000")
    try:
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True,
            use_reloader=True,
            threaded=True
        )
    except Exception as e:
        print(f"服务器启动失败: {str(e)}") 
