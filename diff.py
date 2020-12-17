import os


current_dir = os.getcwd()



old = os.path.join(current_dir, "oic_conn_agent_installer_old/agenthome/lib")
new = os.path.join(current_dir, "oic_conn_agent_installer_new/agenthome/lib")

already_check = []
for filename in os.listdir(old):
    if filename.endswith(".jar") and filename not in already_check:
        print(filename)
        already_check.append(filename)
