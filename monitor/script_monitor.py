import subprocess
import logging
import os

logger = logging.getLogger('script-monitor')

class ScriptMonitor:
    def __init__(self, scripts):
        self.scripts = scripts
        self.processes = {}

    def start_script(self, path):
        name = os.path.basename(path)
        logger.info(f"Starting {name}......")
        try:
            process=subprocess.Popen(['python3', path])
            self.processes[name] = {'path': path, 'process': process}
        except Exception as e:
            logger.error(e)

    def check_scripts(self):
        for script in self.scripts:
            path=script['path']
            restart=script.get('restart_on_failure', False)

            name = os.path.basename(path)

            # Retrieve the script from processes dict
            scriptData = self.processes.get(name)
            if not scriptData:
                logger.warning(f"{name} is not running")
                if restart:
                    logger.info(f"Starting {name}")
                    self.start_script(path)
                continue
            
            # Get the script process 
            process = scriptData['process']

            process_dead = process.poll() is not None
            
            if process_dead:
                logger.warning(f"{name} crashed....")
                if restart:
                    logger.info(f"Restarting {name}")
                    self.start_script(path)