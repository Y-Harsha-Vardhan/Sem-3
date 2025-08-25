% Clearing workspace and closing all previously opened figures
clear;
clc;
close all;

% --- Step 1.1: Generating the clean sine wave ---
x = -3:0.02:3; % Range of x, from -3 to 3 in steps of 0.02
y = 6.5 * sin(2.1 * x + pi/3); % Sine Curve Equation

% --- Step 1.2: Generating the corrupted sine wave (f = 30%) ---
f = 0.30;
n = length(y); % Total number of data points
z = y; % Initializing z as a copy of the clean signal

% Calculating the number of points to corrupt (30% of the points)
num_corrupt = round(f * n);

% Selecting indices at random to corrupt using randperm
indices_to_corrupt = randperm(n, num_corrupt);

% Generating random noise values between 100 and 120 using rand
noise = 100 + (120 - 100) * rand(1, num_corrupt);

% Replacing the values at the selected indices with the noise generated
z(indices_to_corrupt) = noise;



% --Step 2: Applying the three filters (mean, median and first quartile) --
w = 8; % The neighborhood width (8 to the left, 8 to the right)
y_median = zeros(1, n);
y_mean = zeros(1, n);
y_quartile = zeros(1, n);

for i = 1:n
    % Defining the start and end of the neighborhood
    % max/min functions handle the edges of the signal
    start_index = max(1, i - w);
    end_index = min(n, i + w);
    
    % Extracting the neighborhood from the corrupted signal z
    neighborhood = z(start_index:end_index);
    
    % Calculating the statistic for each filter
    y_median(i) = median(neighborhood);
    y_mean(i) = mean(neighborhood);
    y_quartile(i) = quantile(neighborhood, 0.25); % 0.25 for first quartile
end


% --- Step 3.1: Plotting the signals for f=30% ---
figure; % Creating a new figure window
hold on; % Allowing multiple plots on the same figure

% Plotting corrupted signal as white dots
plot(x, z, 'w-', 'DisplayName', 'Corrupted Signal'); 
plot(x, y, 'b-', 'LineWidth', 2, 'DisplayName', 'Original Signal');
plot(x, y_median, 'r-', 'LineWidth', 1.5, 'DisplayName', 'Median Filtered');
plot(x, y_mean, 'g-', 'LineWidth', 1.5, 'DisplayName', 'Mean Filtered');
plot(x, y_quartile, 'm-', 'LineWidth', 1.5, 'DisplayName', 'Quartile Filtered');

title('Signal Filtering (f = 30% Corruption)');
xlabel('x');
ylabel('Signal Value');
legend('show'); % Displaying the legend
grid on;
hold off;

% --- Step 3.2: Calculating and displaying the RMSE ---
rmse_median = sum((y - y_median).^2) / sum(y.^2);
rmse_mean = sum((y - y_mean).^2) / sum(y.^2);
rmse_quartile = sum((y - y_quartile).^2) / sum(y.^2);

fprintf('--- Results for f = 30%% ---\n');
fprintf('RMSE Median Filter: %f\n', rmse_median);
fprintf('RMSE Mean Filter:   %f\n', rmse_mean);
fprintf('RMSE Quartile Filter: %f\n\n', rmse_quartile);


% --- Repeating all steps for f = 60% ---

% --- Step 1: Generating the corrupted sine wave (f = 60%) ---
f = 0.60;
z = y; % Starting with a clean copy again

% Calculating the number of points to corrupt
num_corrupt = round(f * n);

% Getting random indices to corrupt using randperm
indices_to_corrupt = randperm(n, num_corrupt);

% Generating random noise values between 100 and 120
noise = 100 + (120 - 100) * rand(1, num_corrupt);

% Replacing the values with noise
z(indices_to_corrupt) = noise;

% -- Step 2: Applying the three filters (mean, median and first quartile)--
for i = 1:n
    start_index = max(1, i - w);
    end_index = min(n, i + w);
    neighborhood = z(start_index:end_index);
    
    y_median(i) = median(neighborhood);
    y_mean(i) = mean(neighborhood);
    y_quartile(i) = quantile(neighborhood, 0.25);
end

% --- Step 3.1: Plotting the signals for f=60% ---
figure;
hold on;
plot(x, z, 'w-', 'DisplayName', 'Corrupted Signal');
plot(x, y, 'b-', 'LineWidth', 2, 'DisplayName', 'Original Signal');
plot(x, y_median, 'r-', 'LineWidth', 1.5, 'DisplayName', 'Median Filtered');
plot(x, y_mean, 'g-', 'LineWidth', 1.5, 'DisplayName', 'Mean Filtered');
plot(x, y_quartile, 'm-', 'LineWidth', 1.5, 'DisplayName', 'Quartile Filtered');

title('Signal Filtering (f = 60% Corruption)');
xlabel('x');
ylabel('Signal Value');
legend('show');
grid on;
hold off;

% --- Step 3.2: Calculating and showing the RMSE ---
rmse_median = sum((y - y_median).^2) / sum(y.^2);
rmse_mean = sum((y - y_mean).^2) / sum(y.^2);
rmse_quartile = sum((y - y_quartile).^2) / sum(y.^2);

fprintf('--- Results for f = 60%% ---\n');
fprintf('RMSE Median Filter: %f\n', rmse_median);
fprintf('RMSE Mean Filter:   %f\n', rmse_mean);
fprintf('RMSE Quartile Filter: %f\n', rmse_quartile);