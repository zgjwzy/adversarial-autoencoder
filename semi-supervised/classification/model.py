# -*- coding: utf-8 -*-
from args import args
import aae
from aae_semi_supervised import AAE, Conf

conf = Conf()
conf.gpu_enabled = True if args.gpu_enabled == 1 else False
conf.learning_rate_for_reconstruction_cost = 0.0001
conf.learning_rate_for_adversarial_cost = 0.0001
conf.learning_rate_for_semi_supervised_cost = 0.0001
conf.momentum_for_reconstruction_cost = 0.1
conf.momentum_for_adversarial_cost = 0.1
conf.momentum_for_semi_supervised_cost = 0.1
conf.wscale = 0.1
conf.gradient_clipping = 5.0
conf.ndim_z = 10
conf.ndim_y = 10

conf.batchnorm_before_activation = True

conf.generator_shared_hidden_units = [1000]
conf.generator_hidden_units = [1000]
conf.generator_activation_function = "elu"
conf.generator_apply_dropout = False
conf.generator_apply_batchnorm = False
conf.generator_apply_batchnorm_to_input = False

conf.decoder_hidden_units = [1000, 1000]
conf.decoder_activation_function = "elu"
conf.decoder_apply_dropout = False
conf.decoder_apply_batchnorm = False
conf.decoder_apply_batchnorm_to_input = False

conf.discriminator_z_hidden_units = [1000, 1000]
conf.discriminator_z_activation_function = "elu"
conf.discriminator_z_apply_dropout = False
conf.discriminator_z_apply_batchnorm = False
conf.discriminator_z_apply_batchnorm_to_input = False

conf.discriminator_y_hidden_units = [1000, 1000]
conf.discriminator_y_activation_function = "elu"
conf.discriminator_y_apply_dropout = False
conf.discriminator_y_apply_batchnorm = False
conf.discriminator_y_apply_batchnorm_to_input = False

conf.q_z_x_type = aae.Q_Z_X_TYPE_GAUSSIAN

aae = AAE(conf, name="aae")
aae.load(args.model_dir)
