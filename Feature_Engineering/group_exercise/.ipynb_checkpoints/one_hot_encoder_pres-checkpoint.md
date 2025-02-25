# <span style="color:lightgreen"> __One hot encoder__ </span>


## What is one hot encoder and what does it do?

This transforms categorical (nominal/ordinal) variables into a matrix of binary $(0/1)$ variables. For the purpose of this activity, we worked with a dataset which should be familiar to all of us  - the "penguins" data.


When we look at this data, we see some categorical columns, specifically:
* species
* island
* sex

The one hot encoder works by taking each unique entry from a categorical column and generating a new column with a $1$ if that entry was placed and a $0$ if it was not. Syntactically, this is done as follows:

```python
#This example is for the "species" column

#Create a data frame out of the column(s) we want to transform
cols = df[['species']]
cols

#define the ohc transformer
#use this for a general initialization
ohc = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

#use this if you want to have it drop the first column automatically 
#(discussed later in the warnings section)
ohc = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')

#.fit will identify what ohc is pulling from
ohc.fit(cols)   

#if you want to list the categories it identified, you can do so with .categories_
ohc.categories_

#Now actually transform the columns to the 0/1. This is done with .transform
t = ohc.transform(cols)
print(t.shape)
print()
t

#You can then format this output as a data frame
species_df = pd.DataFrame(t, columns=ohc.get_feature_names_out()) #this will make the columns have name format 
                                                               #species_{entry} for each entry

# species.head() if you wan to preview it / look it over

```
The end result is a data frame which contains columns for each unique entry of the original column(s) indicated with $0/1$ entries indicating True/False values for whether each entry is there. These can then be merged into the original data frame as new features.

## Merging with original data frame

This is done via concatonation. The syntax for this is as follows, where our original data frame is called "df" and the new one we created with this encoding is species_df. 

```python
new_df = pd.concat([df, species_df], axis=1)
```

## Drawbacks/Warning

Here we must check for colinearity (or dependence) between these new "features." For example, if there are only three possible islands, the result for the third island column is completely determined by the first two. This can be taken care of by including the 

```python
drop='first' 
```

argument in the first position when initializing the one hot encoder
