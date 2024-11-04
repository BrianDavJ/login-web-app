from appSrc import create_app 

app = create_app()

if __name__ == '__main__':
    print("Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.endpoint}")
    app.run(debug=True)