#Folder Directories

def return_dir(dataset, classification):

    #Directories for binary classification from the CWRU dataset
    if dataset == "CWRU" and classification == "binary":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\CWRU\\"
        normal_data = ["normal_0\\DE", "normal_0\\FE", "normal_1\\DE", "normal_1\\FE"]
        fault_data = ["IR021_12k_BA\\0_DE_BA", "IR021_12k_BA\\0_FE_BA", "IR021_12k_BA\\1_DE_BA", "IR021_12k_BA\\1_FE_BA",
                 "IR021_12k_DE\\0_DE_DE", "IR021_12k_DE\\0_FE_DE", "IR021_12k_DE\\1_DE_DE", "IR021_12k_DE\\1_FE_DE",
                 "IR021_12k_FE\\0_DE_FE", "IR021_12k_FE\\0_FE_FE", "IR021_12k_FE\\1_DE_FE", "IR021_12k_FE\\1_FE_FE"]
        return folder_dir, normal_data, fault_data

    #Directories for binary classification from the HIT dataset
    elif dataset == "HIT" and classification == "binary":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\HIT\\"
        normal_data = ["data1\\3", "data1\\4", "data1\\5", "data1\\6"]
        fault_data = ["data3\\3", "data3\\4", "data3\\5", "data3\\6"]
        return folder_dir, normal_data, fault_data

    #Directories for binary classification from the XJTU-SY dataset
    elif dataset == "XJTU-SY" and classification == "binary":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\XJTU-SY\\"
        normal_data = ["Bearing2_1\\Horizontal_Normal", "Bearing2_1\\Vertical_Normal"]
        fault_data = ["Bearing2_1\\Horizontal_Fault", "Bearing2_1\\Vertical_Fault"]
        return folder_dir, normal_data, fault_data

    #Directories for dataset classifcation including all datasets
    elif dataset == "all" and classification == "dataset":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\"
        
        CWRU_dir = ["CWRU\\normal_0\\DE", "CWRU\\normal_0\\FE", "CWRU\\normal_1\\DE", "CWRU\\normal_1\\FE", 
                    "CWRU\\IR021_12k_BA\\0_DE_BA", "CWRU\\IR021_12k_BA\\0_FE_BA", "CWRU\\IR021_12k_DE\\0_DE_DE", "CWRU\\IR021_12k_DE\\0_FE_DE",
                    "CWRU\\IR021_12k_FE\\0_DE_FE", "CWRU\\IR021_12k_FE\\0_FE_FE"]

        HIT_dir = ["HIT\\data1\\3", "HIT\\data1\\5", 
                   "HIT\\data3\\3", "HIT\\data3\\5", 
                   "HIT\\data5\\3", "HIT\\data5\\5"]

        XJTU_SY_dir = ["XJTU-SY\\Bearing2_1\\Horizontal_Normal", "XJTU-SY\\Bearing2_1\\Vertical_Normal",
                       "XJTU-SY\\Bearing2_1\\Horizontal_Fault", "XJTU-SY\\Bearing2_1\\Vertical_Fault"]

        return folder_dir, CWRU_dir, HIT_dir, XJTU_SY_dir

    #Directories for bearing type classification from the CWRU dataset
    elif dataset == "CWRU" and classification == "bearing":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\CWRU\\"
        norm_data = ["normal_0\\DE", "normal_0\\FE", "normal_1\\DE", "normal_1\\FE"]
        inner_data = ["IR021_12k_BA\\0_DE_BA", "IR021_12k_BA\\0_FE_BA", "IR021_12k_BA\\1_DE_BA", "IR021_12k_BA\\1_FE_BA",
                      "IR021_12k_DE\\0_DE_DE", "IR021_12k_DE\\0_FE_DE", "IR021_12k_DE\\1_DE_DE", "IR021_12k_DE\\1_FE_DE",
                      "IR021_12k_FE\\0_DE_FE", "IR021_12k_FE\\0_FE_FE", "IR021_12k_FE\\1_DE_FE", "IR021_12k_FE\\1_FE_FE"]
        outer_data = ["OR021@6_0_BA\\0_DE_BA", "OR021@6_0_BA\\0_FE_BA", "OR021@6_0_DE\\0_DE_DE", "OR021@6_0_DE\\0_DE_DE", "OR021@6_0_FE\\0_DE_FE", "OR021@6_0_FE\\0_DE_FE"]
        return folder_dir, norm_data, inner_data, outer_data

    #Directories for bearing type classification from the HIT dataset
    elif dataset == "HIT" and classification == "bearing":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\HIT\\"
        norm_data = ["data1\\3", "data1\\4", "data1\\5", "data1\\6"]
        inner_data = ["data3\\3", "data3\\4", "data3\\5", "data3\\6"]
        outer_data = ["data5\\3", "data5\\4", "data5\\5", "data5\\6"]
        return folder_dir, norm_data, inner_data, outer_data

    #Directories for bearing type classification from the XJTU-SY dataset
    elif dataset == "XJTU-SY" and classification == "bearing":
        folder_dir = "D:\\Final Year Project\\Complete Dataset to Use\\CNN Datasets\\XJTU-SY\\"
        norm_data = ["Bearing2_1\\Horizontal_Normal", "Bearing2_1\\Vertical_Normal",
                    "Bearing2_2\\Horizontal_Normal", "Bearing2_2\\Vertical_Normal"]
        inner_data = ["Bearing2_1\\Horizontal_Fault", "Bearing2_1\\Vertical_Fault"]
        outer_data = ["Bearing2_2\\Horizontal_Fault", "Bearing2_2\\Vertical_Fault"]
        return folder_dir, norm_data, inner_data, outer_data
        
