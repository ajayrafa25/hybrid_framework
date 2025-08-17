Training Pipeline
=================

The training entrypoint is ``train.py``.

Hybrid Workflow
---------------

.. code-block:: python

   if 'runner_type' not in cfg:
       # build the default runner
       runner = Runner.from_cfg(cfg)
   else:
       # build customized runner from the registry
       runner = RUNNERS.build(cfg)

   # start training
   checkpoint_callback = ModelCheckpoint(
       dirpath=cfg.work_dir,
       filename='sample-cifar-{epoch:02d}'
   )

   trainer = Trainer(
       **cfg.trainer,
       strategy="ddp",
       max_epochs=5,
       callbacks=[checkpoint_callback],
       default_root_dir=cfg.work_dir
   )

   trainer.fit(runner.model, runner.train_dataloader)

This combines:
- OpenMMLab’s **Runner** (config-driven initialization of models/dataloaders)
- PyTorch Lightning’s **Trainer** (training loop, checkpointing, distributed training)
