#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Hoang Nghiem 
# DATE CREATED: Jan-18-2021                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    dict_dognames = dict()
    with open(dogfile, 'r') as df:
        for line in df:
            dog_names = line.strip('\r\n')
            dict_dognames[dog_names] = 1
#    print(dict_dognames)
    all_dog_names = list(dict_dognames)
    
    for key,value in results_dic.items():
        results_dic[key].append(compare_with_pet_image_label(all_dog_names, value[0]))
        results_dic[key].append(compare_with_classifier_label(all_dog_names, value[1]))


def compare_with_pet_image_label(all_dog_names, pet_image_label):
    for dog_name in all_dog_names:
        if (pet_image_label in dog_name):
            label_index = dog_name.find(pet_image_label)
#            print("label_index {} of {} in {}".format(label_index, pet_image_label, dog_name))
            if (label_index + len(pet_image_label)) == len(dog_name):
                if (label_index == 0):
#                    print("1.pet image label {} matchs with {}".format(pet_image_label, dog_name))
                    return 1
                elif (dog_name[label_index - 1].isalpha() is False):
#                    print("2.pet image label {} matchs with {}".format(pet_image_label, dog_name))
                    return 1
            elif (label_index + len(pet_image_label)) < len(dog_name):
                if (label_index == 0) and (dog_name[label_index + len(pet_image_label)].isalpha() is False):
#                    print("3.pet image label {} matchs with {}".format(pet_image_label, dog_name))
                    return 1
                elif (label_index > 0) and (dog_name[label_index + len(pet_image_label)].isalpha() is False) and (dog_name[label_index - 1].isalpha() is False):
#                    print("4.pet image label {} matchs with {}".format(pet_image_label, dog_name))
                    return 1
#    print("pet image label {} Found no match".format(pet_image_label))
    return 0

def compare_with_classifier_label(all_dog_names, classifier_label):
    for dog_name in all_dog_names:
        sub_labels = classifier_label.split(',')
        for sub_label in sub_labels:
            if sub_label in dog_name:
                label_index = dog_name.find(sub_label)
#                print("label_index {} of {} in {}".format(label_index, sub_label, dog_name))
                if (label_index + len(sub_label)) == len(dog_name):
                    if (label_index == 0):
#                        print("classifier label {} matchs with {}".format(sub_label, dog_name))
                        return 1
                    elif (dog_name[label_index - 1].isalpha() is False):
#                        print("classifier label {} matchs with {}".format(sub_label, dog_name))
                        return 1
                elif (label_index + len(sub_label)) < len(dog_name):
                    if (label_index == 0) and (dog_name[label_index + len(sub_label)].isalpha() is False):
#                        print("classifier label {} matchs with {}".format(sub_label, dog_name))
                        return 1
                    elif (label_index > 0) and (dog_name[label_index + len(sub_label)].isalpha() is False) and (dog_name[label_index - 1].isalpha() is False):
#                        print("classifier label {} matchs with {}".format(sub_label, dog_name))
                        return 1
#    print("classifier label {} Found no match".format(classifier_label))
    return 0

        
        