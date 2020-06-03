%% Hossein Hassani
%% Started @: 12 Nov 2014
%% Last update @: 27 Dec 2014

function vocabList = getVocabList()
%GETVOCABLIST reads the fixed vocabulary list in KurmanjiSoraniWeighting.txt and returns a
%cell array of the words
%   vocabList = GETVOCABLIST() reads the fixed vocabulary list in KurmanjiSoraniWeighting.txt 
%   and returns a cell array of the words in vocabList.


%% Read the fixed vocabulary list
fid = fopen('KurmanjiSoraniWeighting.txt');

% For ease of implementation, we use a struct to map the strings => integers
% In practice, you'll want to use some form of hashmap

i = 1;
vocabList = cell(i, 1);

while(!feof(fid))
    % Word Index (can ignore since it will be = i)
    fscanf(fid, '%d', 1);
	if(!feof(fid))
		% Actual Word
		vocabList{i} = fscanf(fid, '%s', 1);
		% Ignore the next two weighting items
		fscanf(fid, '%d', 1);
		fscanf(fid, '%d', 1);
		i ++;
	end
end

fclose(fid);

end
