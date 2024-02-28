import sys
import quickfix as fix
import quickfix44 as fix44
import argparse
from loguru import logger

log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.add(sys.stdout, format=log_format, level="INFO")

class KitetsuClient(fix.Application):
    def onCreate(self, sessionID):
        self.sessionID = sessionID
        return

    def onLogon(self, sessionID):
        self.sendTestOrder(sessionID)

    def onLogout(self, sessionID):
        print("Logout - session:", sessionID)

    def toAdmin(self, message, sessionID):
        return

    def fromAdmin(self, message, sessionID):
        return

    def toApp(self, message, sessionID):
        print("Sending message:", message)

    def fromApp(self, message, sessionID):
        print("Received message:", message)

    def sendTestOrder(self, sessionID):
        order = fix44.NewOrderSingle()
        order.setField(fix.ClOrdID("123456"))
        order.setField(fix.HandlInst('1'))
        order.setField(fix.Symbol("AAPL"))
        order.setField(fix.Side(fix.Side_BUY))
        order.setField(fix.TransactTime())
        order.setField(fix.OrderQty(100))
        order.setField(fix.OrdType(fix.OrdType_MARKET))
        
        fix.Session.sendToTarget(order, sessionID)

def main():
    parser = argparse.ArgumentParser(description="Kitetsu QuickFIX Client")
    parser.add_argument('-c', '--config', required=True, help='Path to FIX configuration file')
    parser.add_argument('-l', '--log', required=False, help='Path to log file')
    args = parser.parse_args()
    if 'help' in args:
        parser.print_help()
        return
    config_file = args.config
    log_file = args.log if args.log else "./kitetsu.log"
    logger.add(log_file, format=log_format, level="INFO")

    try:
        settings = fix.SessionSettings(config_file)
        application = KitetsuClient()
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
        initiator.start()
        input("Press <enter> to quit\n")
        initiator.stop()
    except (fix.ConfigError, fix.RuntimeError) as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    main()
