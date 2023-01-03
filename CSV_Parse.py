
import pandas
from numpy import random
import numpy as np
from pandas.core.frame import DataFrame

def csv_parse():
    #root = tk.Tk()
    #root.withdraw()
    #file_path = filedialog.askopenfilename()
    file_path = '/Users/sfoconnor/Desktop/Graduate Assistant/Data/Mechanical and Nuclear Engineering.csv'
    subOut_List = {}
    student_list = []
    write_out = []
    accredidation_add = []
    #Create Dictionary To Hold The Accredidation Standards
    accred_Standards = {}
    accred_Standards['1'] = "1. Apply Principles of Engineering, Science, and Mathematics"
    accred_Standards['2'] = "2. Apply Engineering Design to Meet Specific Needs"
    accred_Standards['3'] = "3. Communicate Effectively"
    accred_Standards['4'] = "4. Ethical and Professional Responsibility and Impact"
    accred_Standards['5'] = "5. Teamwork"
    accred_Standards['6'] = "6. Conduct Experiments, Analyze and Interpret Data"
    accred_Standards['7'] = "7. Acquire and Apply New Knowledge"
    
    
    # Read in the file
    dataIn = pandas.read_csv(file_path)
    #provides the headers for the new csv file
    header_list = list(dataIn)
    header_list.append("Accredidation Standard")
    for index, row in dataIn.iterrows():
        l_outcome = row['learning outcome name']
        #Need to check to make sure it is a valid learning outcome. AKA doesnt start with a number
        toplevel_cat = l_outcome.split('.')[0]
        accred_selected = accred_Standards.get(toplevel_cat)
        #Try to convert to integer. If successful, continue the loop and skip to next row.
        if (not toplevel_cat.isnumeric()):
            continue

        #Now we know that the learning outcome is valid. Can add to dictionary.
        if(not subOut_List.__contains__(l_outcome)):
            subOut_List[l_outcome] = 1
    
        if(subOut_List[l_outcome] != 11):
            #These are the two rows needed to check for blanks. If blank, ignore.
            out_score = row['outcome score']
            master_score = row['learning outcome mastered']
            #These rows need to be manipulated. Check for blanks.
            if(not(np.isnan(out_score) or np.isnan(master_score))):
                #Add Randomly Generated ID Value For New Column. Then Write Column to New CSV File
                student_id = random.randint(low=123456779, high=123456799)
                student_list.append(student_id)
                write_out.append(row)
                accredidation_add.append(accred_selected)
                subOut_List[l_outcome] = subOut_List.get(l_outcome) + 1
            #Continue if either of the two column values are blank
            continue
        continue
    #create a dataframe and write it to a csv file
    d_frame = DataFrame(data=write_out, index=student_list, columns=header_list)
    d_frame.index.name = "Student ID"
    d_frame['Accredidation Standard'] = accredidation_add
    d_frame.to_csv('/Users/sfoconnor/Desktop/Graduate Assistant/Data/NEW_MechE_And_Nuclear.csv')

    #Take the same dataframe and write it to a xlsx file
    writer = pandas.ExcelWriter('/Users/sfoconnor/Desktop/Graduate Assistant/Data/NEW_MechE_And_Nuclear.xlsx')
    d_frame.to_excel(writer, index=student_list, columns=header_list)
    writer.save()
    
csv_parse();