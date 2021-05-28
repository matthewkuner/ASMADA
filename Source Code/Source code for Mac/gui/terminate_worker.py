# -*- coding: utf-8 -*-
import sys

class terminate_worker_class:

    def terminate_worker_command(self):
        """
        If workerThread exists, forces it to terminate.
        """
        
        # Upon completion/termination of analysis, re-enable inputs.
        self.lock_inputs_command(False)
        
        try:
            self.workerThread.stop()
            self.thread.quit()
            self.thread.wait()
        except:
            pass