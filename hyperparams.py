data_path_base = './datasets'
logdir_path = './logdir'


class Default:
    sr = 16000
    frame_shift = 0.005  # seconds
    frame_length = 0.025  # seconds
    n_mfcc = 40  # No of mfcc values
    n_fft = 512

    # 80 samples.  This is dependent on the frame_shift.
    hop_length = int(sr * frame_shift)
    # 400 samples. This is dependent on the frame_length.
    win_length = int(sr * frame_length)

    preemphasis = 0.97
    n_mfcc = 40
    n_iter = 60  # Number of inversion iterations
    n_mels = 80
    duration = 2

    batch_size = 1


class Train1:
    # path
    data_path = '{}/timit/TIMIT/TRAIN/*/*/*.WAV'.format(data_path_base)
    mfccs_file_path = 'mfccs_file_train'
    phns_file_path = 'phns_file_train'

    # model
    hidden_units = 256  # alias = E
    num_banks = 16
    num_highway_blocks = 4
    norm_type = 'ins'  # a normalizer function. value: bn, ln, ins, or None
    t = 1.0  # temperature
    dropout_rate = 0.2

    # train
    batch_size = 1
    lr = 0.0003
    num_epochs = 1000
    save_per_epoch = 2


class Train2:
    # path
    data_path = '{}/kate/sense_and_sensibility_split/*.wav'.format(
        data_path_base)
    # data_path = '{}/arctic/slt/*.wav'.format(data_path_base)

    # model
    hidden_units = 512  # alias = E
    num_banks = 16
    num_highway_blocks = 8
    norm_type = 'ins'  # a normalizer function. value: bn, ln, ins, or None
    t = 1.0  # temperature
    dropout_rate = 0.2

    # train
    batch_size = 1
    lr = 0.0005
    num_epochs = 10000
    save_per_epoch = 50


class Test1:
    # path
    data_path = '{}/timit/TIMIT/TEST/*/*/*.WAV'.format(data_path_base)

    # test
    batch_size = 32

    mfccs_file_path = 'mfccs_file_test'
    phns_file_path = 'phns_file_test'


class Test2:
    # test
    batch_size = 32


class Convert:
    # path
    data_path = '{}/arctic/bdl/*.wav'.format(data_path_base)

    # convert
    batch_size = 2
    emphasis_magnitude = 1.2