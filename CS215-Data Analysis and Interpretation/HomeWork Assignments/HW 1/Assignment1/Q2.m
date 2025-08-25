clear;
clc;

%#####################################################################%

function newMean = UpdateMean(OldMean, NewDataValue, n)
    newMean = (OldMean * n + NewDataValue) / (n + 1);
end

%#####################################################################%

function newMedian = UpdateMedian(OldMedian, NewDataValue, A, n)
    if mod(n, 2) == 1
        if n == 1
            newMedian = (A(1) + NewDataValue) / 2;
            return;
        end
        median_index = (n + 1) / 2;
        A_before = A(median_index - 1);
        A_after = A(median_index + 1);

        if NewDataValue < OldMedian
            newMedian = (OldMedian + max(NewDataValue, A_before)) / 2;
        else 
            newMedian = (OldMedian + min(NewDataValue, A_after)) / 2;
        end
    else
        m1_index = n / 2;
        m2_index = n / 2 + 1;
        m1 = A(m1_index);
        m2 = A(m2_index);
        
        if NewDataValue < m1
            newMedian = m1;
        elseif NewDataValue > m2
            newMedian = m2;
        else 
            newMedian = NewDataValue;
        end
    end
end

%#####################################################################%

function newStd = UpdateStd(OldMean, OldStd, NewMean, NewDataValue, n)
    if n == 0
        newStd = 0; 
        return;
    end
    
    sum_sq_old = (n - 1) * OldStd^2 + n * OldMean^2;   
    sum_sq_new = sum_sq_old + NewDataValue^2;
    
    N = n + 1;
    
    new_variance = (sum_sq_new - N * NewMean^2) / n;
    
    if new_variance < 0
        new_variance = 0;
    end
    
    newStd = sqrt(new_variance);
end

%#####################################################################%
