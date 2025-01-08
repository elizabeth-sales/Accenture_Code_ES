%Creating time series graphs for HIT dataset

%batch_num must be changed manually by user
%batch_num = total number of files

filedir = "**File Directory**";
n = dir(fullfile(filedir, "*.csv"));

%Iterate through all series in one dataset
for h=0:batch_num
    %Importing all data from individual .csv files
    fileName = "**File Directory**" + h + ".csv";
    dataset = readtable(fileName);
    
    %Defining array variables to columns of the dataset
    record = dataset{:,col_num};
    %Remove numerical label row
    record(1,:) = [];
    
    %Creating time variable array
    t = [0, 1:length(record)-1]/25000; %Sample rate of 25000Hz
    %Transpose into column array
    time = t.'; 
    
    %Finding the minimum and maximum values for normalisation
    [minRecord,maxRecord] = bounds(record);
    
    %Normalising using min-max between -1 and 1
    for i=1:length(record)
        record(i,1) = (2 * ((record(i,1) - minRecord)/(maxRecord - minRecord))) -1;
    end
    
    %--Plot the graphs--
    %Increments of 0.1s
    
    %Plot first 0.1s graph seperately due to indexing errors
    f = figure('visible','off'); %Removes axis lines
    plot(time(1:2500), record(1:2500)); 
    
    %Sets size of axes
    axis([0 0.1, -1 1]);
    xticks(0:0.01:0.1);
    yticks([-1 0 1]);
    
    set(gca,'XTick',[], 'YTick', []); %Removes axes values from graph plot
    
    fileNameP1 = "D:\Final Year Project\Complete Dataset to Use\CNN Datasets\HIT\data5\6\figure5_" + h + "_" + "0" + ".jpeg";
    saveas(f,fileNameP1);
    
    %Iterating through half of the samples
    for i=1:3
        j = i+1;
    
        n = i*2500;
        m = j*2500;
        
        f = figure('visible','off'); %Removes axis lines
        plot(time(n:m), record(n:m));
        
        %Sets size of axes based on segment of data
        axis([(i/10) (j/10), -1 1]);
        xticks((i/10):0.01:(j/10));
        yticks([-1 0 1]);
        
        set(gca,'XTick',[], 'YTick', []); %Removes axes values from graph plot

        filenameP2 = "D:\Final Year Project\Complete Dataset to Use\CNN Datasets\HIT\data5\6\figure5_" + h + '_' + i + ".jpeg";
        saveas(f,filenameP2);
    
    end

end