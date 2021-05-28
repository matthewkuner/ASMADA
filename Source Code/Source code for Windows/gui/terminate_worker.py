# -*- coding: utf-8 -*-

class terminate_worker_class:

    def terminate_worker_command(self):
        """
        If workerThread exists, forces it to terminate.
        """
        
        # Upon completion/termination of analysis, re-enable inputs.
        self.lock_inputs_command(False)
        
        try:
            self.workerThread.stop()
            self.workerThread.quit
        except:
            pass
        
        
    def analysis_terminated_message_command(self):
        """
        If "Stop Analysis" button is pushed, display that the analysis has
        been cancelled.
        """

        self.analysis_status_progress_label_1.setText('')
        self.analysis_status_progress_label_2.setText('analysis terminated')