"""
Callbacks
=========

Callbacks supported by Lightning
"""

import abc


class Callback(abc.ABC):
    """Abstract base class used to build new callbacks."""

    def on_init_start(self, trainer, pl_module):
        """Called when the trainer initialization begins."""
        assert pl_module is None

    def on_init_end(self, trainer, pl_module):
        """Called when the trainer initialization ends."""
        pass

    def on_fit_start(self, trainer, pl_module):
        """Called when the fit begins."""
        pass

    def on_fit_end(self, trainer, pl_module):
        """Called when the fit ends."""
        pass

    def on_epoch_start(self, trainer, pl_module):
        """Called when the epoch begins."""
        pass

    def on_epoch_end(self, trainer, pl_module):
        """Called when the epoch ends."""
        pass

    def on_batch_start(self, trainer, pl_module):
        """Called when the training batch begins."""
        pass

    def on_batch_end(self, trainer, pl_module):
        """Called when the training batch ends."""
        pass

    def on_train_start(self, trainer, pl_module):
        """Called when the train begins."""
        pass

    def on_train_end(self, trainer, pl_module):
        """Called when the train ends."""
        pass

    def on_validation_start(self, trainer, pl_module):
        """Called when the validation loop begins."""
        pass

    def on_validation_end(self, trainer, pl_module):
        """Called when the validation loop ends."""
        pass

    def on_test_start(self, trainer, pl_module):
        """Called when the test begins."""
        pass

    def on_test_end(self, trainer, pl_module):
        """Called when the test ends."""
        pass
