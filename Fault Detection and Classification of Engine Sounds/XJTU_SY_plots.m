%Create plots for the XJTU-SY Dataset

%batch_num must be changed manually by user
%batch_num = total number of files

%Iterate through individual CSV files
for h=1:batch_num
    dataset = readtable("**File Directory**" + h + ".csv");
    
    %Defining array variables to columns of the dataset
    record = dataset{:,2};

    %Creating time variable array
    t = [0, 1:length(record)-1]/25600; %Sample rate of 25000Hz
    %Transpose into column array
    time = t.'; 
    
    %Finding the minimum and maximum values for normalisation
    [minRecord,maxRecord] = bounds(record);
    
    %Normalising using min-max between -1 and 1
    for i=1:length(record)
        record(i,1) = (2 * ((record(i,1) - minRecord)/(maxRecord - minRecord))) -1;
    end
    
    %--Plot the graphs--
    %Increments of 0.2s
    
    %Plot first 0.2s graph seperately due to indexing errors
    f = figure('visible','off');
    plot(time(1:5120), record(1:5120));
    
    %Sets size of axes
    axis([0 0.2, -1 1]);
    xticks(0:0.02:0.2);
    yticks([-1 0 1]);

    set(gca,'XTick',[], 'YTick', []); %Removes axes values from graph plot
    
    filename = "D:\Final Year Project\Complete Dataset to Use\CNN Datasets\XJTU-SY\Bearing2_2\Vertical\" + h + "_" + "0.jpeg";
    saveas(f,filename);
    
    %Iterating through all samples
    for i= 1:(30720/5120)-1
        j = i+1;
    
        n = i*5120;
        m = j*5120;
    
        f = figure('visible','off');
        plot(time(n:m), record(n:m));
        
        %Sets size of axes
        axis([(i/5) (j/5), -1 1]);
        xticks((i/5):0.02:(j/5));
        yticks([-1 0 1]);

        set(gca,'XTick',[], 'YTick', []); %Removes axes values from graph plot
    
        filename = "D:\Final Year Project\Complete Dataset to Use\CNN Datasets\XJTU-SY\Bearing2_2\Vertical\" + h + "_" + i + ".jpeg";
        saveas(f,filename);
    
    end
end








