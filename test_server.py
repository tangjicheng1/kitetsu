import quickfix as fix
import argparse

class TestServer(fix.Application):
    def onCreate(self, sessionID):
        return

    def onLogon(self, sessionID):
        print("Logon:", sessionID)

    def onLogout(self, sessionID):
        print("Logout:", sessionID)

    def toAdmin(self, session, message):
        return

    def fromAdmin(self, session, message):
        print("Admin Message Received:", message)

    def toApp(self, session, message):
        print("Sending Application Message:", message)

    def fromApp(self, message, sessionID):
        print("Application Message Received:", message)

def main(config_file):
    try:
        settings = fix.SessionSettings(config_file)
        application = TestServer()
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.ScreenLogFactory(settings)
        acceptor = fix.SocketAcceptor(application, storeFactory, settings, logFactory)
        acceptor.start()
        # Keep the server running until manually interrupted
        input("Press <enter> to quit\n")
        acceptor.stop()
    except (fix.ConfigError, fix.RuntimeError) as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QuickFIX Test Server")
    parser.add_argument('-c', '--config', required=True, help='Path to server configuration file')
    args = parser.parse_args()
    
    main(args.config)
