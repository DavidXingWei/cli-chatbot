from chatbot import Chatbot,ROLES

def main():
    print("可用角色：",", ".join(ROLES.keys()))
    role=input("选择角色(回车用default): ").strip() or "default"
    bot=Chatbot(role=role)
    print(f"你选择了角色: {bot.role}")
    print("命令：/exit/clear/role")
    print("-" * 40)
    try:
        while True:
            user_input = input("你: ").strip()
            if not user_input:
                continue
            if user_input == "exit":
                print("再见！")
                break
            if user_input == "clear":
                bot.clear_history()
                continue
            if user_input == "/role":
                print("可用角色：", ", ".join(ROLES.keys()))
                new_role =input("输入新角色：").strip()
                if new_role in ROLES:
                    bot = Chatbot(role=new_role)
                    print(f"角色已切换到: {bot.role}")
                else:
                    print("无效角色，保持当前角色不变。")
                continue
            response = bot.generate_response(user_input)
            print(f"Chatbot: {response}\n")
    except KeyboardInterrupt:
        print("\n再见！")   
if __name__ == "__main__":
    main()