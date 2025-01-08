%Creating time series graphs for CWRU dataset

%Importing all data from individual .csv files
dataset = readtable('**File directory**');

%Defining array variables to columns of the dataset
time = dataset{:,1}/12000; %Sample rate of 12000Hz
record = dataset{:,2};

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
plot(time(1:sample_rate_div), record(1:sample_rate_div)); 

%Sets size of axes
axis([0 0.1, -1 1])
xticks(0:0.01:0.1)
yticks([-1 0 1])

set(gca,'XTick',[], 'YTick', []); %Removes axes values from graph plot

saveas(f,'figure0','jpeg');

%Iterating through all samples
for i=1:(len(record)/sample_rate_div)-1
    j = i+1;

    n = i*sample_rate_div;
    m = j*sample_rate_div;
    
    f = figure('visible','off'); %Removes axis lines
    plot(time(n:m), record(n:m));
    
    %Sets size of axes based on segment of data
    axis([(i/10) (j/10), -1 1]);
    xticks((i/10):0.01:(j/10));
    yticks([-1 0 1]);
    
    set(gca,'XTick',[], 'YTick', []); %Removes axes values from graph plot
    
    filename = "figure" + i + ".jpeg";
    saveas(f,filename);

end
