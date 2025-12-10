import yaml
import logging
from monitor import ScriptMonitor


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='/Users/victoronowho/devops_learning/logs/scriptlog.log',
    filemode='a',
    level=logging.DEBUG
)

logger = logging.getlogger('self_heal')