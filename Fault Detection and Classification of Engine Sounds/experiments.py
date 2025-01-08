#Experiments List

#Function to return details for single experiment
def return_experiment_array(number):
    experiments = [
        #CNN
        #Binary classification:
        #CWRU
        ["lenet5", (8,16), "CWRU", "binary", "CNN\\binary_CWRU_lenet816_acc.png", "CNN\\binary_CWRU_lenet816_loss.png"],
        ["lenet5", (16,32), "CWRU", "binary", "CNN\\binary_CWRU_lenet1632_acc.png", "CNN\\binary_CWRU_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32), "CWRU", "binary", "CNN\\binary_CWRU_3LA81632_acc.png", "CNN\\binary_CWRU_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128), "CWRU", "binary", "CNN\\binary_CWRU_3LA3264128_acc.png", "CNN\\binary_CWRU_3LA3264128_loss.png"],
        ["vgg", (0), "CWRU", "binary", "CNN\\binary_CWRU_vgg_acc.png", "CNN\\binary_CWRU_vgg_loss.png"],
        #HIT
        ["lenet5", (8,16), "HIT", "binary", "CNN\\binary_HIT_lenet816_acc.png", "CNN\\binary_HIT_lenet816_loss.png"],
        ["lenet5", (16,32), "HIT", "binary", "CNN\\binary_HIT_lenet1632_acc.png", "CNN\\binary_HIT_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32), "HIT", "binary", "CNN\\binary_HIT_3LA81632_acc.png", "CNN\\binary_HIT_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128), "HIT", "binary", "CNN\\binary_HIT_3LA3264128_acc.png", "CNN\\binary_HIT_3LA3264128_loss.png"],
        ["vgg", (0), "HIT", "binary", "CNN\\binary_HIT_vgg_acc.png", "CNN\\binary_HIT_vgg_loss.png"],
        #XJTU-SY
        ["lenet5", (8,16), "XJTU-SY", "binary", "CNN\\binary_XJTU_SY_lenet816_acc.png", "CNN\\binary_XJTU_SY_lenet816_loss.png"],
        ["lenet5", (16,32), "XJTU-SY", "binary", "CNN\\binary_XJTU_SY_lenet1632_acc.png", "CNN\\binary_XJTU_SY_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32),  "XJTU-SY", "binary", "CNN\\binary_XJTU_SY_3LA81632_acc.png", "CNN\\binary_XJTU_SY_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128),  "XJTU-SY", "binary", "CNN\\binary_XJTU_SY_3LA3264128_acc.png", "CNN\\binary_XJTU_SY_3LA3264128_loss.png"],
        ["vgg", (0),  "XJTU-SY", "binary", "CNN\\binary_XJTU_SY_vgg_acc.png", "CNN\\binary_XJTU_SY_vgg_loss.png"],
        #Dataset classification:
        ["lenet5", (8,16), "all", "dataset", "CNN\\dataset_lenet816_acc.png", "CNN\\dataset_lenet816_loss.png"],
        ["lenet5", (16,32), "all", "dataset", "CNN\\dataset_lenet1632_acc.png", "CNN\\dataset_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32), "all", "dataset", "CNN\\dataset_3LA81632_acc.png", "CNN\\dataset_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128), "all", "dataset", "CNN\\dataset_3LA3264128_acc.png", "CNN\\dataset_3LA3264128_loss.png"],
        ["vgg", (0), "all", "dataset", "CNN\\dataset_vgg_acc.png", "CNN\\dataset_vgg_loss.png"],
        #Bearing classification:
        #CWRU
        ["lenet5", (8,16), "CWRU", "bearing", "CNN\\bearing_CWRU_lenet816_acc.png", "CNN\\bearing_CWRU_lenet816_loss.png"],
        ["lenet5", (16,32), "CWRU", "bearing", "CNN\\bearing_CWRU_lenet1632_acc.png", "CNN\\bearing_CWRU_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32), "CWRU", "bearing", "CNN\\bearing_CWRU_3LA81632_acc.png", "CNN\\bearing_CWRU_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128), "CWRU", "bearing", "CNN\\bearing_CWRU_3LA3264128_acc.png", "CNN\\bearing_CWRU_3LA3264128_loss.png"],
        ["vgg", (0), "CWRU", "bearing", "CNN\\bearing_CWRU_vgg_acc.png", "CNN\\bearing_CWRU_vgg_loss.png"],
        #HIT
        ["lenet5", (8,16), "HIT", "bearing", "CNN\\bearing_HIT_lenet816_acc.png", "CNN\\bearing_HIT_lenet816_loss.png"],
        ["lenet5", (16,32), "HIT", "bearing", "CNN\\bearing_HIT_lenet1632_acc.png", "CNN\\bearing_HIT_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32), "HIT", "bearing", "CNN\\bearing_HIT_3LA81632_acc.png", "CNN\\bearing_HIT_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128), "HIT", "bearing", "CNN\\bearing_HIT_3LA3264128_acc.png", "CNN\\bearing_HIT_3LA3264128_loss.png"],
        ["vgg", (0), "HIT", "bearing", "CNN\\bearing_HIT_vgg_acc.png", "CNN\\bearing_HIT_vgg_loss.png"],
        #XJTU-SY
        ["lenet5", (8,16), "XJTU-SY", "bearing", "CNN\\bearing_XJTU_SY_lenet816_acc.png", "CNN\\bearing_XJTU_SY_lenet816_loss.png"],
        ["lenet5", (16,32), "XJTU-SY", "bearing", "CNN\\bearing_XJTU_SY_lenet1632_acc.png", "CNN\\bearing_XJTU_SY_lenet1632_loss.png"],
        ["three_layer_alt", (8,16,32), "XJTU-SY", "bearing", "CNN\\bearing_XJTU_SY_3LA81632_acc.png", "CNN\\bearing_XJTU_SY_3LA81632_loss.png"],
        ["three_layer_alt", (32,64,128), "XJTU-SY", "bearing", "CNN\\bearing_XJTU_SY_3LA3264128_acc.png", "CNN\\bearing_XJTU_SY_3LA3264128_loss.png"],
        ["vgg", (0), "XJTU-SY", "bearing", "CNN\\bearing_XJTU_SY_vgg_acc.png", "CNN\\bearing_XJTU_SY_vgg_loss.png"],
        
        #ANN
        #Binary classification:
        #CWRU
        ["ann3232", (32,32), "CWRU", "binary", "ANN\\binary_CWRU_ann3232_acc.png", "ANN\\binary_CWRU_ann3232_loss.png"],
        ["ann6432", (64,32), "CWRU", "binary", "ANN\\binary_CWRU_ann6432_acc.png", "ANN\\binary_CWRU_ann6432_loss.png"],
        ["ann161616", (16,16,16), "CWRU", "binary", "ANN\\binary_CWRU_ann161616_acc.png", "ANN\\binary_CWRU_ann161616_loss.png"],
        ["ann32168", (32,16,8), "CWRU", "binary", "ANN\\binary_CWRU_ann32168_acc.png", "ANN\\binary_CWRU_ann32168_loss.png"],
        #HIT
        ["ann3232", (32,32), "HIT", "binary", "ANN\\binary_HIT_ann3232_acc.png", "ANN\\binary_HIT_ann3232_loss.png"],
        ["ann6432", (64,32), "HIT", "binary", "ANN\\binary_HIT_ann6432_acc.png", "ANN\\binary_HIT_ann6432_loss.png"],
        ["ann161616", (16,16,16), "HIT", "binary", "ANN\\binary_HIT_ann161616_acc.png", "ANN\\binary_HIT_ann161616_loss.png"],
        ["ann32168", (32,16,8), "HIT", "binary", "ANN\\binary_HIT_ann32168_acc.png", "ANN\\binary_HIT_ann32168_loss.png"],
        #XJTU-SY
        ["ann3232", (32,32), "XJTU-SY", "binary", "ANN\\binary_XJTU_SY_ann3232_acc.png", "ANN\\binary_XJTU_SY_ann3232_loss.png"],
        ["ann6432", (64,32), "XJTU-SY", "binary", "ANN\\binary_XJTU_SY_ann6432_acc.png", "ANN\\binary_XJTU_SY_ann6432_loss.png"],
        ["ann161616", (16,16,16), "XJTU-SY", "binary", "ANN\\binary_XJTU_SY_ann161616_acc.png", "ANN\\binary_XJTU_SY_ann161616_loss.png"],
        ["ann32168", (32,16,8), "XJTU-SY", "binary", "ANN\\binary_XJTU_SY_ann32168_acc.png", "ANN\\binary_XJTU_SY_ann32168_loss.png"],
        #Dataset classification:
        ["ann3232", (32,32), "all", "dataset", "ANN\\dataset_ann3232_acc.png", "ANN\\dataset_ann3232_loss.png"],
        ["ann6432", (64,32), "all", "dataset", "ANN\\dataset_ann6432_acc.png", "ANN\\dataset_ann6432_loss.png"],
        ["ann161616", (16,16,16), "all", "dataset", "ANN\\dataset_ann161616_acc.png", "ANN\\dataset_ann161616_loss.png"],
        ["ann32168", (32,16,8), "all", "dataset", "ANN\\dataset_ann32168_acc.png", "ANN\\dataset_ann32168_loss.png"],
        #Bearing classification:
        #CWRU
        ["ann3232", (32,32), "CWRU", "bearing", "ANN\\bearing_CWRU_ann3232_acc.png", "ANN\\bearing_CWRU_ann3232_loss.png"],
        ["ann6432", (64,32), "CWRU", "bearing", "ANN\\bearing_CWRU_ann6432_acc.png", "ANN\\bearing_CWRU_ann6432_loss.png"],
        ["ann161616", (16,16,16), "CWRU", "bearing", "ANN\\bearing_CWRU_ann161616_acc.png", "ANN\\bearing_CWRU_ann161616_loss.png"],
        ["ann32168", (32,16,8), "CWRU", "bearing", "ANN\\bearing_CWRU_ann32168_acc.png", "ANN\\bearing_CWRU_ann32168_loss.png"],
        #HIT
        ["ann3232", (32,32), "HIT", "bearing", "ANN\\bearing_HIT_ann3232_acc.png", "ANN\\bearing_HIT_ann3232_loss.png"],
        ["ann6432", (64,32), "HIT", "bearing", "ANN\\bearing_HIT_ann6432_acc.png", "ANN\\bearing_HIT_ann6432_loss.png"],
        ["ann161616", (16,16,16), "HIT", "bearing", "ANN\\bearing_HIT_ann161616_acc.png", "ANN\\bearing_HIT_ann161616_loss.png"],
        ["ann32168", (32,16,8), "HIT", "bearing", "ANN\\bearing_HIT_ann32168_acc.png", "ANN\\bearing_HIT_ann32168_loss.png"],
        #XJTU-SY
        ["ann3232", (32,32), "XJTU-SY", "bearing", "ANN\\bearing_XJTU_SY_ann3232_acc.png", "ANN\\bearing_XJTU_SY_ann3232_loss.png"],
        ["ann6432", (64,32), "XJTU-SY", "bearing", "ANN\\bearing_XJTU_SY_ann6432_acc.png", "ANN\\bearing_XJTU_SY_ann6432_loss.png"],
        ["ann161616", (16,16,16), "XJTU-SY", "bearing", "ANN\\bearing_XJTU_SY_ann161616_acc.png", "ANN\\bearing_XJTU_SY_ann161616_loss.png"],
        ["ann32168", (32,16,8), "XJTU-SY", "bearing", "ANN\\bearing_XJTU_SY_ann32168_acc.png", "ANN\\bearing_XJTU_SY_ann32168_loss.png"],

        #SNN
        #Binary classification:
        #CWRU
        ["snn646432", (64,64,32), "CWRU", "binary", "SNN\\binary_CWRU_snn646432_acc.png", "SNN\\binary_CWRU_snn646432_loss.png"],
        ["snn323216", (32,32,16), "CWRU", "binary", "SNN\\binary_CWRU_snn323216_acc.png", "SNN\\binary_CWRU_snn323216_loss.png"],
        ["snn16168", (16,16,8), "CWRU", "binary", "SNN\\binary_CWRU_snn16168_acc.png", "SNN\\binary_CWRU_snn16168_loss.png"],
        #HIT
        ["snn646432", (64,64,32), "HIT", "binary", "SNN\\binary_HIT_snn646432_acc.png", "SNN\\binary_HIT_snn646432_loss.png"],
        ["snn323216", (32,32,16), "HIT", "binary", "SNN\\binary_HIT_snn323216_acc.png", "SNN\\binary_HIT_snn323216_loss.png"],
        ["snn16168", (16,16,8), "HIT", "binary", "SNN\\binary_HIT_snn16168_acc.png", "SNN\\binary_HIT_snn16168_loss.png"],
        #XJTU-SY
        ["snn646432", (64,64,32), "XJTU-SY", "binary", "SNN\\binary_XJTU_SY_snn646432_acc.png", "SNN\\binary_XJTU_SY_snn646432_loss.png"],
        ["snn323216", (32,32,16), "XJTU-SY", "binary", "SNN\\binary_XJTU_SY_snn323216_acc.png", "SNN\\binary_XJTU_SY_snn323216_loss.png"],
        ["snn16168", (16,16,8), "XJTU-SY", "binary", "SNN\\binary_XJTU_SY_snn16168_acc.png", "SNN\\binary_XJTU_SY_snn16168_loss.png"],
        #Dataset classification:
        ["snn646432", (64,64,32), "all", "dataset", "SNN\\dataset_snn646432_acc.png", "SNN\\dataset_snn646432_loss.png"],
        ["snn323216", (32,32,16), "all", "dataset", "SNN\\dataset_snn323216_acc.png", "SNN\\dataset_snn323216_loss.png"],
        ["snn16168", (16,16,8), "all", "dataset", "SNN\\dataset_snn16168_acc.png", "SNN\\dataset_snn16168_loss.png"],
        #Bearing classification:
        #CWRU
        ["snn646432", (64,64,32), "CWRU", "bearing", "SNN\\bearing_CWRU_snn646432_acc.png", "SNN\\bearing_CWRU_snn646432_loss.png"],
        ["snn323216", (32,32,16), "CWRU", "bearing", "SNN\\bearing_CWRU_snn323216_acc.png", "SNN\\bearing_CWRU_snn323216_loss.png"],
        ["snn16168", (16,16,8), "CWRU", "bearing", "SNN\\bearing_CWRU_snn16168_acc.png", "SNN\\bearing_CWRU_snn16168_loss.png"],
        #HIT
        ["snn646432", (64,64,32), "HIT", "bearing", "SNN\\bearing_HIT_snn646432_acc.png", "SNN\\bearing_HIT_snn646432_loss.png"],
        ["snn323216", (32,32,16), "HIT", "bearing", "SNN\\bearing_HIT_snn323216_acc.png", "SNN\\bearing_HIT_snn323216_loss.png"],
        ["snn16168", (16,16,8), "HIT", "bearing", "SNN\\bearing_HIT_snn16168_acc.png", "SNN\\bearing_HIT_snn16168_loss.png"],
        #XJTU-SY
        ["snn646432", (64,64,32), "XJTU-SY", "bearing", "SNN\\bearing_XJTU_SY_snn646432_acc.png", "SNN\\bearing_XJTU_SY~_snn646432_loss.png"],
        ["snn323216", (32,32,16), "XJTU-SY", "bearing", "SNN\\bearing_XJTU_SY_snn323216_acc.png", "SNN\\bearing_XJTU_SY_snn323216_loss.png"],
        ["snn16168", (16,16,8), "XJTU-SY", "bearing", "SNN\\bearing_XJTU_SY_snn16168_acc.png", "SNN\\bearing_XJTU_SY_snn16168_loss.png"]
    ]

    return experiments[number]
