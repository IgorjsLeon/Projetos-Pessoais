import pyautogui
import time
import pyperclip

#===================================DICIONARIOS===================================

def dicionarios():
    inversores_220v = {'AC10-T/S2-R75G-B':'220V, 0,75Kw, 1CV, 4A',
              'AC10-T/S2-1R5G-B':'220V, 1,5Kw, 2CV, 7A',
              'AC10-T/S2-2R2G-B':'220V, 2,2Kw, 3CV, 10A',
              'AC310-T/S2-1R5G-B':'220V, 1,5Kw, 2CV, 7A',
              'AC310-T/S2-2R2G-B':'220V, 2,2Kw, 3CV, 10A',
              'AC310-T/S2-004G-B':'220V, 4Kw, 5,5CV, 16A',
              'AC310-T/S2-5R5G-B':'220V, 5,5Kw, 7,5CV, 20A',
              'AC310-T/S2-7R5G-B':'220V, 7,5Kw, 10CV, 30A',
              'AC310-T/S2-011G-B':'220V, 11Kw, 15CV, 42A',
              'AC310-T/S2-015G':'220V, 15Kw, 20CV, 55A',
              'AC310-T2-018G':'220V, 18Kw, 25CV, 70A',
              'AC310-T2-022G':'220V, 22Kw, 30CV, 80A',
              'AC310-T2-030G':'220V, 30Kw, 40CV, 110A',
              'AC310-T2-037G':'220V, 37Kw, 50CV, 130A',
              'AC310-T2-055G':'220V, 55Kw, 75CV, 200A'}

    inversores_380_440v = {'AC10-T3-R75G-B':'380V, 0,75Kw, 1CV, 3A',
                       'AC10-T3-1R5G-B':'380V, 1,5Kw, 2CV, 4A',
                       'AC10-T3-2R2G-B':'380V, 2,2Kw, 3CV, 5A',
                       'AC10-T3-004G-B':'380V, 4Kw, 5,5CV, 9,5A',
                       'AC10-T3-5R5G-B':'380V, 5,5Kw, 7,5CV, 13A',
                       'AC10-T3-7R5G-B':'380V, 7,5Kw, 10CV, 17A',
                       'AC310-T3-1R5G/2R2P-B':'380V, 1,5Kw, 2CV, 4A',
                       'AC310-T3-2R2G-B':'380V, 2,2Kw, 3CV, 6A',
                       'AC310-T3-004G/5R5P-B':'380V, 4Kw, 5,5CV, 10A',
                       'AC310-T3-5R5G/7R5P-B':'380V, 5,5Kw, 7,5CV, 13A',
                       'AC310-T3-7R5G/011P-B':'380V, 7,5Kw, 10CV, 17A',
                       'AC310-T3-011G/015P-B':'380V, 11Kw, 15CV, 25A',
                       'AC310-T3-015G/018P-B':'380V, 15Kw, 20CV, 32A',
                       'AC310-T3-018G/022P-B':'380V, 18Kw, 25CV, 38A',
                       'AC310-T3-022G/030P-B':'380V, 22Kw, 30CV, 45A',
                       'AC310-T3-030G/037P':'380V, 30Kw, 40CV, 60A',
                       'AC310-T3-037G/045P':'380V, 37Kw, 50CV, 75A',
                       'AC310-T3-045G/055P':'380V, 45Kw, 60CV, 90A',
                       'AC310-T3-055G/075P':'380V, 55Kw, 75CV, 110A',
                       'AC310-T3-075G/090P':'380V, 75Kw, 100CV, 150A',
                       'AC310-T3-090G/110P':'380V, 90Kw, 125CV, 180A',
                       'AC310-T3-110G/132P':'380V, 110Kw, 150CV, 210A',
                       'AC310-T3-132G/160P-L':'380V, 132Kw, 175CV, 250A',
                       'AC310-T3-160G/185P-L':'380V, 160Kw, 200CV, 310A',
                       'AC310-T3-185G/200P-L':'380V, 185Kw, 250CV, 340A',
                       'AC310-T3-200G/220P-L':'380V, 200Kw, 275CV, 380A',
                       'AC310-T3-220G/250P-L':'380V, 220Kw, 300CV, 410A',
                       'AC310-T3-280G/315P-L':'380V, 280Kw, 350CV, 510A'}
    
    soft220v = {'SSV-100-S4-022':'220V, 43A, 15CV',
            'SSV-100-S4-045':'220V, 90A, 30CV',
            'SSV-100-S4-075':'220V, 150A, 50CV',
            'SSV-100-S4-115':'220V, 230A, 75CV',
            'SSV-100-S4-160':'220V, 320A, 125CV',
            'SSV-100-S4-220':'220V, 500A, 200CV'}
    
    soft380_440v = {'SSV-100-S4-022':'380V, 43A, 30CV',
            'SSV-100-S4-045':'380V, 90A, 60CV',
            'SSV-100-S4-075':'380V, 150A, 100CV',
            'SSV-100-S4-115':'380V, 230A, 150CV',
            'SSV-100-S4-160':'380V, 320A, 250CV',
            'SSV-100-S4-220':'380V, 500A, 300CV'}
    
    encoder = {'Encoder Inc mod H40-8-0100 VL1':'100 pulsos (5-24VDC)  1M cabo',
               'Encoder Inc mod H40-8-0500 VL1':'500 pulsos (5-24VDC)  1M cabo',
               'Encoder Inc mod H40-8-1000 VL1':'1000 pulsos (5-24VDC)  1M cabo'
    }

    kit_Servodrive220 = {'SD700-P1-B-004-36-005-W':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo BASE, SEM FREIO',
                         'SD700-S1-B-004-36-005-W':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N1-B-004-36-005-W':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E1-B-004-36-005-W':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P1-B-004-36-005-W-B':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo BASE, COM FREIO',
                         'SD700-S1-B-004-36-005-W-B':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo STANDARD, COM FREIO',
                         'SD700-N1-B-004-36-005-W-B':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo PROFINET, COM FREIO',
                         'SD700-E1-B-004-36-005-W-B':'220V, 0,4 Kw, 1,25 Nm, 3000/6000 RPM, Flange 60mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P1-C-008-34-005-W':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo BASE, SEM FREIO',
                         'SD700-S1-C-008-34-005-W':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N1-C-008-34-005-W':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E1-C-008-34-005-W':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P1-C-008-34-005-W-B':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo BASE, COM FREIO',
                         'SD700-S1-C-008-34-005-W-B':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo STANDARD, COM FREIO',
                         'SD700-N1-C-008-34-005-W-B':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo PROFINET, COM FREIO',
                         'SD700-E1-C-008-34-005-W-B':'220V, 0,75Kw, 2,4Nm, 3000/4500 RPM, Flange 80mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P2-E-010-23-005-W':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, SEM FREIO',
                         'SD700-S2-E-010-23-005-W':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N2-E-010-23-005-W':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E2-E-010-23-005-W':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P2-E-010-23-005-W-B':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, COM FREIO',
                         'SD700-S2-E-010-23-005-W-B':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, COM FREIO',
                         'SD700-N2-E-010-23-005-W-B':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, COM FREIO',
                         'SD700-E2-E-010-23-005-W-B':'220V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P2-E-012-35-005-W':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo BASE, SEM FREIO',
                         'SD700-S2-E-012-35-005-W':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N2-E-012-35-005-W':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E2-E-012-35-005-W':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P2-E-012-35-005-W-B':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo BASE, COM FREIO',
                         'SD700-S2-E-012-35-005-W-B':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo STANDARD, COM FREIO',
                         'SD700-N2-E-012-35-005-W-B':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo PROFINET, COM FREIO',
                         'SD700-E2-E-012-35-005-W-B':'220V, 1,2Kw, 3,8 Nm, 3000/5000 RPM, Flange 110mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P2-E-020-23-005-Y':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, SEM FREIO',
                         'SD700-S2-E-020-23-005-Y':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N2-E-020-23-005-Y':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E2-E-020-23-005-Y':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P2-E-020-23-005-Y-B':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, COM FREIO',
                         'SD700-S2-E-020-23-005-Y-B':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, COM FREIO',
                         'SD700-N2-E-020-23-005-Y-B':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, COM FREIO',
                         'SD700-E2-E-020-23-005-Y-B':'220V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P2-E-030-23-005-Y':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, SEM FREIO',
                         'SD700-S2-E-030-23-005-Y':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N2-E-030-23-005-Y':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E2-E-030-23-005-Y':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P2-E-030-23-005-Y-B':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, COM FREIO',
                         'SD700-S2-E-030-23-005-Y-B':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, COM FREIO',
                         'SD700-N2-E-030-23-005-Y-B':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, COM FREIO',
                         'SD700-E2-E-030-23-005-Y-B':'220V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, COM FREIO',
                        
                         'SD700-P2-F-044-72-005-Y':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo BASE, SEM FREIO',
                         'SD700-S2-F-044-72-005-Y':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo STANDAR, SEM FREIO',
                         'SD700-N2-F-044-72-005-Y':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E2-F-044-72-005-Y':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P2-F-044-72-005-Y-B':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo BASE, COM FREIO',
                         'SD700-S2-F-044-72-005-Y-B':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo STANDARD, COM FREIO',
                         'SD700-N2-F-044-72-005-Y-B':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo PROFINET, COM FREIO',
                         'SD700-E2-F-044-72-005-Y-B':'220V, 4,4Kw, 28 Nm, 1500/2000 RPM, Flange 180mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P2-F-055-78-005-Y':'220V, 5,5Kw, 35 Nm, 1500/1800 RPM, Flange 180mm, Modelo BASE, SEM FREIO',
                         'SD700-S2-F-055-78-005-Y':'220V, 5,5Kw, 35 Nm, 1500/1800 RPM, Flange 180mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N2-F-055-78-005-Y':'220V, 5,5Kw, 35 Nm, 1500/1800 RPM, Flange 180mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E2-F-055-78-005-Y':'220V, 5,5Kw, 35 Nm, 1500/1800 RPM, Flange 180mm, Modelo ETHERCAT, SEM FREIO',            
                         }
    
    kit_Servodrive380 = {'SD700-P3-E-010-23-005-W':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, SEM FREIO',
                         'SD700-S3-E-010-23-005-W':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N3-E-010-23-005-W':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E3-E-010-23-005-W':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P3-E-010-23-005-W-B':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, COM FREIO',
                         'SD700-S3-E-010-23-005-W-B':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, COM FREIO',
                         'SD700-N3-E-010-23-005-W-B':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, COM FREIO',
                         'SD700-E3-E-010-23-005-W-B':'380V, 1,0Kw, 4,8 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P3-E-020-23-005-W':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, SEM FREIO',
                         'SD700-S3-E-020-23-005-W':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N3-E-020-23-005-W':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E3-E-020-23-005-W':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P3-E-020-23-005-W-B':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, COM FREIO',
                         'SD700-S3-E-020-23-005-W-B':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, COM FREIO',
                         'SD700-N3-E-020-23-005-W-B':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, COM FREIO',
                         'SD700-E3-E-020-23-005-W-B':'380V, 2,0Kw, 9,6 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P3-E-030-23-005-Y':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, SEM FREIO',
                         'SD700-S3-E-030-23-005-Y':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N3-E-030-23-005-Y':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E3-E-030-23-005-Y':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P3-E-030-23-005-Y-B':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo BASE, COM FREIO',
                         'SD700-S3-E-030-23-005-Y-B':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo STANDARD, COM FREIO',
                         'SD700-N3-E-030-23-005-Y-B':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo PROFINET, COM FREIO',
                         'SD700-E3-E-030-23-005-Y-B':'380V, 3,0Kw, 14,4 Nm, 2000/3000 RPM, Flange 130mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P3-F-044-73-005-Y':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo BASE, SEM FREIO',
                         'SD700-S3-F-044-73-005-Y':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N3-F-044-73-005-Y':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E3-F-044-73-005-Y':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P3-F-044-73-005-Y-B':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo BASE, COM FREIO',
                         'SD700-S3-F-044-73-005-Y-B':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo STANDARD, COM FREIO',
                         'SD700-N3-F-044-73-005-Y-B':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo PROFINET, COM FREIO',
                         'SD700-E3-F-044-73-005-Y-B':'380V, 4,4Kw, 28 Nm, 1500/3000 RPM, Flange 180mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P3-F-055-73-005-Y':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo BASE, SEM FREIO',
                         'SD700-S3-F-055-73-005-Y':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N3-F-055-73-005-Y':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E3-F-055-73-005-Y':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P3-F-055-73-005-Y-B':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo BASE, COM FREIO',
                         'SD700-S3-F-055-73-005-Y-B':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo STANDARD, COM FREIO',
                         'SD700-N3-F-055-73-005-Y-B':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo PROFINET, COM FREIO',
                         'SD700-E3-F-055-73-005-Y-B':'380V, 5,5Kw, 35 Nm, 1500/3000 RPM, Flange 180mm, Modelo ETHERCAT, COM FREIO',

                         'SD700-P3-F-075-73-005-Y':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo BASE, SEM FREIO',
                         'SD700-S3-F-075-73-005-Y':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo STANDARD, SEM FREIO',
                         'SD700-N3-F-075-73-005-Y':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo PROFINET, SEM FREIO',
                         'SD700-E3-F-075-73-005-Y':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo ETHERCAT, SEM FREIO',
                         'SD700-P3-F-075-73-005-Y-B':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo BASE, COM FREIO',
                         'SD700-S3-F-075-73-005-Y-B':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo STANDARD, COM FREIO',
                         'SD700-N3-F-075-73-005-Y-B':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo PROFINET, COM FREIO',
                         'SD700-E3-F-075-73-005-Y-B':'380V, 7,5Kw, 47 Nm, 1500/3000 RPM, Flange 180mm, Modelo ETHERCAT, COM FREIO',
                         }

    indicadores_digitais = {
        "Indicador digital Mini DPM": "Indicações Disponíveis: (HZ / RPM / MPM / V / A / %)",
        "Indicador digital Master DPM": "Indicações Disponíveis: (HZ / RPM / MPM / V / A / %)",
        "Indicador digital DPM-1": "Indicações Disponíveis: (HZ / RPM / MPM / V / A / %)"
    }

    return inversores_220v, inversores_380_440v, soft220v, soft380_440v, encoder, kit_Servodrive220, kit_Servodrive380, indicadores_digitais

#===================================MENUS===================================

def menu_geral():
    menu = True
    while menu:
        print ("#################################################")
        print ("#                                               #")
        print ("#       Envios de orçamento com Python          #")
        print ("#                by Igor Leon                   #")
        print ("#                                               #")
        print ("#                                               #")
        print ("#       1- Orçamento via WhatsApp               #")
        print ("#       2- Orçamento via E-mail                 #")
        print ("#       3- Fechar Programa                      #")
        print ("#                                               #")
        print ("#################################################\n")
        menuwhatsapp = True
        menuemail = True
        menuresposta= True
        while menuresposta:
            resposta = input("Digite a opção desejada: ")
            if resposta == '1':
                menuresposta = False
                menu_whatsapp()
            elif resposta == '2':
                menuresposta = False
                menu_email()
            elif resposta == '3':
                print ('Fechando programa!')
                menuresposta = False
                menu = False
            else:
                print('Opção Inválida.')
            
def menu_whatsapp():
    print("\n#######################################")
    print('#                                     #')
    print("# Bem vindo ao Orçamento por Whatsapp #")
    print('#                                     #')
    print("# 1- Passar Orçamento                 #")
    print("# 2- Voltar para o Menu de Orçamentos #")
    print('#                                     #')
    print('#######################################\n')
    menurespostawhats = True
    while menurespostawhats:
        resposta = input('Digite a opção desejada: ')
        if resposta == '1':
            menurespostawhats = False
            orcamentos_whats()
        elif resposta == '2':
            menurespostawhats = False
        else:
            print('Opção Inválida.')

def menu_email():
    print("\n#######################################")
    print('#                                     #')
    print("# Bem vindo ao Orçamento por E-mail   #")
    print('#                                     #')
    print("# 1- Passar Orçamento                 #")
    print("# 2- Voltar para o Menu de Orçamentos #")
    print('#                                     #')
    print('#######################################\n')
    menurespostaemail = True
    while menurespostaemail:
        resposta = input('Digite a opção desejada: ')
        if resposta == '1':
            menurespostaemail = False
            orcamentos_email()
        elif resposta == '2':
            menurespostaemail = False
        else:
            print('Opção Inválida.')

def menu_materiais(materiais):
    print("\n################################################")
    print('#                                                #')
    print("#        Escolha de material                     #")
    print('#                                                #')
    print("# 1- Inversores (AC10 e AC310)                   #")
    print("# 2- Soft Starter                                #")
    print("# 3- Encoder's (100, 500, 1000)                  #")
    print("# 4- Indicadores Digitais (Mini, Master e DPM-1) #")
    print("# 5- Kit's ServoDrive   (220V / 380V)            #")
    print("# 6- Outros Produtos                             #")
    print('#                                                #')
    print('##################################################\n')
    menurespostamateriais = True
    while menurespostamateriais:
        resposta = int(input('Digite a opção desejada: '))
        if resposta == 1:
            menurespostamateriais = False
            inversores(materiais)
        elif resposta == 2:
            menurespostamateriais = False
            soft(materiais)
        elif resposta == 3:
            menurespostamateriais = False
            menu_encoder(materiais)
        elif resposta == 4:
            menurespostamateriais = False
            menu_indicadores(materiais)
        elif resposta == 5:
            menurespostamateriais = False
            kit_servo(materiais)
        elif resposta == 6:
            menurespostamateriais = False
            outros_materiais(materiais)
        else:
            print("Opção Inválida.")
    
def menu_encoder(materiais):
    print("\n#######################################")
    print('#                                     #')
    print("# 1- Encoder 100 pulsos               #")
    print("# 2- Encoder 500 pulsos               #")
    print("# 3- Encoder 1000 pulsos              #")
    print('#                                     #')
    print('#######################################\n')
    respostamenuencoder = True
    while respostamenuencoder:
        respostamenuenc = int(input('Digite a opção desejada: '))
        if respostamenuenc == 1:
            respostamenuencoder = False
            encoder(materiais, respostamenuenc)
        elif respostamenuenc == 2:
            respostamenuencoder = False
            encoder(materiais, respostamenuenc)
        elif respostamenuenc == 3:
            respostamenuencoder = False
            encoder(materiais, respostamenuenc)
        else:
            print("Opção Inválida.")

def menu_indicadores(materiais):
    print("\n#######################################")
    print('#                                     #')
    print("# 1- Mini DPM                         #")
    print("# 2- Master DPM                       #")
    print("# 3- DPM-1                            #")
    print('#                                     #')
    print('#######################################\n')
    while True:
        try:
            respostamenuindicador = int(input('Digite a opção desejada: '))
            if respostamenuindicador in [1, 2, 3]:
                indicadores_digitais(materiais, respostamenuindicador)
                break  # Sai do loop após processamento
            else:
                print("Opção Inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

#===================================BUSCAS NOS DICIONARIOS===================================

def busca_inversor220v(modelo_parcial, cv):
    inversores_220v, _, _, _, _, _, _, _ = dicionarios()
    modelo_parcial = modelo_parcial.upper()
    cv_formatado = formata_cv(cv)
    
    for modelo, descricao in inversores_220v.items():
        modelo_match = modelo_parcial in modelo
        descricao_formatada = formata_descricao(descricao)
        cv_match = cv_formatado in descricao_formatada
        
        if modelo_match and cv_match:
            return modelo, descricao

    return None, None

def busca_inversor380_440v(modelo_parcial, cv):
    _, inversores_380_440v, _, _, _, _, _, _ = dicionarios()
    modelo_parcial = modelo_parcial.upper()
    cv_formatado = formata_cv(cv)
    
    for modelo, descricao in inversores_380_440v.items():
        modelo_match = modelo_parcial in modelo
        descricao_formatada = formata_descricao(descricao)
        cv_match = cv_formatado in descricao_formatada
        
        if modelo_match and cv_match:
            return modelo, descricao

    return None, None

def busca_soft220v(modelo_parcial, cv):
    _, _, soft220v, _, _, _, _, _ = dicionarios()
    modelo_parcial = modelo_parcial.upper()
    cv = f'{cv}CV'
        
    for modelo, descricao in soft220v.items():     
        modelo_match = modelo_parcial in modelo
        cv_match = cv in descricao
        
        if modelo_match and cv_match:
            return modelo, descricao
    
    return None, None

def busca_soft380_440v(modelo_parcial, cv):
    _, _, _, soft380_440v, _, _, _, _ = dicionarios()
    modelo_parcial = modelo_parcial.upper()
    cv = f'{cv}CV'
        
    for modelo, descricao in soft380_440v.items():     
        modelo_match = modelo_parcial in modelo
        cv_match = cv in descricao
        
        if modelo_match and cv_match:
            return modelo, descricao
    
    return None, None

def busca_encoder(modelo_parcial, quant_pulsos):
    _, _, _, _, encoder, _, _, _ = dicionarios()
    quant_pulsos = f'{quant_pulsos} pulsos'
        
    for modelo, descricao in encoder.items():     
        modelo_match = modelo_parcial in modelo
        quant_pulsos_match = quant_pulsos in descricao
        
        if modelo_match and quant_pulsos_match:
            return modelo, descricao
    
    return None, None

def busca_kit220v(chave):
    _, _, _, _, _, kit_Servodrive220, _, _ = dicionarios()
    
    # Buscando o modelo diretamente pela chave gerada
    if chave in kit_Servodrive220:
        return chave, kit_Servodrive220[chave]
    else:
        print("Chave não encontrada no dicionário.")
        return None, None

def busca_kit380v(chave):
    _, _, _, _, _, _, kit_Servodrive380, _ = dicionarios()
        # Buscando o modelo diretamente pela chave gerada
    if chave in kit_Servodrive380:
        return chave, kit_Servodrive380[chave]
    else:
        print("Chave não encontrada no dicionário.")
        return None, None

def busca_indicadores(modelo_parcial):
    _, _, _, _, _, _, _, indicadores_digitais = dicionarios()
    
    for modelo, descricao in indicadores_digitais.items():
        if modelo_parcial.lower() in modelo.lower():
            return modelo, descricao

    return None, None

#===================================TEXTOS PARA ORÇAMENTOS===================================

def texto_orcamento_email(cliente, forma_pagamento, materiais):
    texto =  f"""Prezado(a) {cliente}.\n
Agradecemos o interesse em nossos produtos/serviços. Conforme solicitado, segue o orçamento detalhado:
    \nDescrição do Produto/Serviço:\n"""

    total_geral = 0

    for idx, mat in enumerate(materiais, start=1):
        modelo = mat['modelo']
        descricao_material = mat['descricao_material']
        quantidade = mat['quantidade']
        valor_final_c_ipi = mat['valor_final_c_ipi']
        valor_IPI = mat['valor_IPI']
        valor_quantidade = mat['valor_quantidade']

        if valor_IPI != '0':
            texto += f"""
Produto/Serviço {idx}: {modelo} ({descricao_material})
Quantidade: {quantidade}
Valor Unitário: R${formatar_valor(valor_final_c_ipi)} + {valor_IPI}% IPI
Valor: R${formatar_valor(valor_quantidade)}\n"""

            total_geral += valor_quantidade
        else:
            texto += f"""
Produto/Serviço {idx}: {modelo} ({descricao_material})
Quantidade: {quantidade}
Valor Unitário: R${formatar_valor(valor_final_c_ipi)}
Valor: R${formatar_valor(valor_quantidade)}\n"""

            total_geral += valor_quantidade

    texto += f"""
===============================\n
    Resumo do Orçamento:\n
Total Geral: R${formatar_valor(total_geral)}\n
Salientamos que o Difal de ICMS ou Substituição Tributária (ST) não estão inclusos no valor apresentado. Caso venham a ser aplicáveis, o valor poderá sofrer alterações.
\n===============================\n
    Forma de Pagamento:\n
{forma_pagamento}\n
Frete não incluso! (FOB)\n
Indicar Transportadora ou Portador de sua confiança!
\n===============================\n
Aguardamos sua confirmação para dar prosseguimento.\n
Atenciosamente,\n
Igor
Departamento de Vendas
Veder
    """
    return texto

def texto_orcamento_wsp(cliente, forma_pagamento, materiais):
    texto =  f"""Prezado(a) {cliente}.\n
Agradecemos o interesse em nossos produtos/serviços. Conforme solicitado, segue o orçamento detalhado:
    \n*Descrição do Produto/Serviço:*\n"""

    total_geral = 0

    for idx, mat in enumerate(materiais, start=1):
        modelo = mat['modelo']
        descricao_material = mat['descricao_material']
        quantidade = mat['quantidade']
        valor_final_c_ipi = mat['valor_final_c_ipi']
        valor_IPI = mat['valor_IPI']
        valor_quantidade = mat['valor_quantidade']

        if valor_IPI != '0':
            texto += f"""
Produto/Serviço {idx}: {modelo} ({descricao_material})
Quantidade: {quantidade}
*Valor Unitário: R${formatar_valor(valor_final_c_ipi)} + {valor_IPI}% IPI* 
Valor: R${formatar_valor(valor_quantidade)}\n"""
            
            total_geral += valor_quantidade
        else:
            texto += f"""
Produto/Serviço {idx}: {modelo} ({descricao_material})
Quantidade: {quantidade}
*Valor Unitário: R${formatar_valor(valor_final_c_ipi)}*
Valor: R${formatar_valor(valor_quantidade)}\n"""

            total_geral += valor_quantidade

    texto += f"""
===============================\n
    *Resumo do Orçamento:*\n
Total Geral: R${formatar_valor(total_geral)}\n
Salientamos que o *Difal de ICMS* ou *Substituição Tributária (ST)* não estão inclusos no valor apresentado. Caso venham a ser aplicáveis, *o valor poderá sofrer alterações.*
\n===============================\n
    *Forma de Pagamento:*\n
*{forma_pagamento}*
*Frete não incluso! (FOB)*
*Indicar Transportadora ou Portador de sua confiança!*
\n===============================\n
Aguardamos sua confirmação para dar prosseguimento.\n
Atenciosamente,\n
Igor
Departamento de Vendas
*Veder*
    """
    return texto

#===================================CALCULOS===================================

def conta_IPI(valor, valor_IPI):
    if valor_IPI == '9.75' or valor_IPI == '9,75':
        valor_final_c_ipi = valor / 1.0975
        return valor_final_c_ipi
    elif valor_IPI == '6.5' or valor_IPI == '6,5':
        valor_final_c_ipi = valor / 1.065
        return valor_final_c_ipi
    elif valor_IPI == '3.25' or valor_IPI == '3,25':
        valor_final_c_ipi = valor / 1.0325
        return valor_final_c_ipi

#===================================FUNÇÕES PARA MENU DE MATERIAIS===================================

def inversores(materiais):
    material = input('Digite o nome do material: ').strip().lower()
    tensao = int(input('Digite a tensão do material (220/380/440): '))

    modelo = None
    descricao_material = None

    if tensao == 220:
        if material == 'ac10':
            cv = input("Digite a quantidade de CV (1, 2, 3): ").replace(',', '.')
            quantidade = int(input('Digite a quantidade do material: '))
            valor = converter_valor(input('Digite o valor do item com IPI: '))
            valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
            valor_quantidade = valor * quantidade
            modelo, descricao_material = busca_inversor220v(material, cv)
        elif material == 'ac310':
            cv = input("Digite a quantidade de CV (2, 3, 5,5, 7,5, 10, 15, 20, 25, 30, 40, 50, 75): ").replace(',', '.')
            quantidade = int(input('Digite a quantidade do material: '))
            valor = converter_valor(input('Digite o valor do item com IPI: '))
            valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
            valor_quantidade = valor * quantidade
            modelo, descricao_material = busca_inversor220v(material, cv)

    elif tensao in (380, 440):
        if material == 'ac10':
            cv = input("Digite a quantidade de CV (1, 2, 3, 5,5, 7,5, 10): ").replace(',', '.')
            quantidade = int(input('Digite a quantidade do material: '))
            valor = float(input('Digite o valor do item com IPI: '))
            valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
            valor_quantidade = valor * quantidade
            modelo, descricao_material = busca_inversor380_440v(material, cv)
        elif material == 'ac310':
            cv = input("Digite a quantidade de CV (2, 3, 5,5, 7,5, 10, 15, 20, 25, 30, 40, 50, 75, 100,\n                           125, 150, 175, 200, 250, 275, 300, 350): ").replace(',', '.')
            quantidade = int(input('Digite a quantidade do material: '))
            valor = float(input('Digite o valor do item com IPI: '))
            valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
            valor_quantidade = valor * quantidade
            modelo, descricao_material = busca_inversor380_440v(material, cv)
    else:
        print('\nTensão inválida!\n')

    if not modelo:
        print('\nMaterial não encontrado.\n')
    
    if valor_IPI != '0':
        valor_final_c_ipi = conta_IPI(valor, valor_IPI)
    else:
        valor_final_c_ipi = valor

    materiais.append({
        'modelo': modelo,
        'descricao_material': descricao_material,
        'quantidade': quantidade,
        'valor_final_c_ipi': valor_final_c_ipi,
        'valor_IPI': valor_IPI,
        'valor_quantidade': valor_quantidade
    })

def soft(materiais):
    material = 'SSV'
    tensao = int(input('Digite a tensão do material (220/380/440): '))

    modelo = None
    descricao_material = None

    if tensao == 220:
        cv = input("Digite a quantidade de CV (15, 30, 50, 75, 125, 200): ")
        quantidade = int(input('Digite a quantidade do material: '))
        valor = converter_valor(input('Digite o valor do item com IPI: '))
        valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
        valor_quantidade = valor * quantidade
        modelo, descricao_material = busca_soft220v(material, cv)
    elif tensao in (380, 440):
        cv = input("Digite a quantidade de CV (30, 60, 100, 150, 250, 300): ")
        quantidade = int(input('Digite a quantidade do material: '))
        valor = converter_valor(input('Digite o valor do item com IPI: '))
        valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
        valor_quantidade = valor * quantidade
        modelo, descricao_material = busca_soft380_440v(material, cv)
    else:
        print('\nTensão inválida!\n')

    if not modelo:
        print('\nMaterial não encontrado.\n')
    
    if valor_IPI != '0':
        valor_final_c_ipi = conta_IPI(valor, valor_IPI)
    else:
        valor_final_c_ipi = valor

    materiais.append({
        'modelo': modelo,
        'descricao_material': descricao_material,
        'quantidade': quantidade,
        'valor_final_c_ipi': valor_final_c_ipi,
        'valor_IPI': valor_IPI,
        'valor_quantidade': valor_quantidade
    })

def encoder(materiais, respostamenuenc):
    quantidade = int(input('Digite a quantidade do material: '))
    valor = converter_valor(input('Digite o valor do item com IPI: '))
    valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
    valor_quantidade = valor * quantidade
    modelo_parcial = 'Encoder Inc mod H40-8-'

    quant_pulsos = None
    
    if respostamenuenc == 1:
        quant_pulsos = 100
    elif respostamenuenc == 2:
        quant_pulsos = 500
    elif respostamenuenc == 3:
        quant_pulsos = 1000

    modelo, descricao_material = busca_encoder(modelo_parcial, quant_pulsos)

    if not modelo:
        print('\nMaterial não encontrado.\n')
        return

    if valor_IPI != '0':
        valor_final_c_ipi = conta_IPI(valor, valor_IPI)
    else:
        valor_final_c_ipi = valor

    materiais.append({
        'modelo': modelo,
        'descricao_material': descricao_material,
        'quantidade': quantidade,
        'valor_final_c_ipi': valor_final_c_ipi,
        'valor_IPI': valor_IPI,
        'valor_quantidade': valor_quantidade
    })

def indicadores_digitais(materiais, respostamenuindicador):
    quantidade = int(input('Digite a quantidade do material: '))
    valor = converter_valor(input('Digite o valor do item com IPI: '))
    valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
    valor_quantidade = valor * quantidade

    modelo_opcoes = {
        1: 'Mini DPM',
        2: 'Master DPM',
        3: 'DPM-1'
    }
    modelo_parcial = modelo_opcoes.get(respostamenuindicador)

    if modelo_parcial:
        modelo, descricao_material = busca_indicadores('Indicador digital ' + modelo_parcial)

        if not modelo:
            print('\nMaterial não encontrado.\n')
            return

        if valor_IPI != '0':
            valor_final_c_ipi = conta_IPI(valor, valor_IPI)
        else:
            valor_final_c_ipi = valor

        materiais.append({
            'modelo': modelo,
            'descricao_material': descricao_material,
            'quantidade': quantidade,
            'valor_final_c_ipi': valor_final_c_ipi,
            'valor_IPI': valor_IPI,
            'valor_quantidade': valor_quantidade
        })
    else:
        print('\nOpção de modelo inválida.\n')

def kit_servo(materiais):
    vmaterial = input("Digite o modelo do Kit (BASE, STANDARD, PROFINET, ETHERCAT):").strip().upper()
    pergunta_freio = input('Com freio ou sem? (c / s): ').strip().lower()
    tensao = int(input('Digite a tensão do material (220/380/440): '))

    # Determinando o sufixo do freio
    if pergunta_freio == 'c':
        sufixo_freio = '-B'  # Indicativo de que tem freio
    elif pergunta_freio == 's':
        sufixo_freio = '-W'  # Indicativo de que não tem freio
    else:
        print("Opção de freio inválida. Use 'c' para com freio ou 's' para sem freio.")
        return


    # Definir a parte da chave relacionada ao modelo
    if tensao == 220:
        kw = input("Digite a quantidade de Kw (0,4, 0,75, 1,0, 1,2, 2,0, 3,0, 4,4, 5,5): ").strip().replace(",", ".")
        # Base para o código SD700
        base_material = 'SD700'
        if kw == '0,4' or kw == '0,75':
            if vmaterial == "BASE":
                modelo_chave = "P1" 
            elif vmaterial == "STANDARD":
                modelo_chave = "S1"
            elif vmaterial == "PROFINET":
                modelo_chave = "N1"
            elif vmaterial == "ETHERCAT":
                modelo_chave = "E1"
            else:
                print("Modelo inválido.")
                return
        else:
            if vmaterial == "BASE":
                modelo_chave = "P2" 
            elif vmaterial == "STANDARD":
                modelo_chave = "S2"
            elif vmaterial == "PROFINET":
                modelo_chave = "N2"
            elif vmaterial == "ETHERCAT":
                modelo_chave = "E2"
            else:
                print("Modelo inválido.")
                return
    elif tensao == 380:
        kw = input("Digite a quantidade de Kw (1,0, 2,0, 3,0, 4,4, 5,5): ").strip().replace(",", ".")
        # Base para o código SD700
        base_material = 'SD700'
        if vmaterial == "BASE":
            modelo_chave = "P3" 
        elif vmaterial == "STANDARD":
            modelo_chave = "S3"
        elif vmaterial == "PROFINET":
            modelo_chave = "N3"
        elif vmaterial == "ETHERCAT":
            modelo_chave = "E3"
        else:
            print("Modelo inválido.")
            return

    # Construindo a chave de acordo com a tensão e o Kw
    if tensao == 220:
        if pergunta_freio == 's':
            if kw == "0.4":
                chave_gerada = f'{base_material}-{modelo_chave}-B-004-36-005{sufixo_freio}'
            elif kw == "0.75":
                chave_gerada = f'{base_material}-{modelo_chave}-C-008-36-005{sufixo_freio}'
            elif kw == "1.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-010-23-005{sufixo_freio}'
            elif kw == "1.2":
                chave_gerada = f'{base_material}-{modelo_chave}-E-012-35-005{sufixo_freio}'
            elif kw == "2.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-020-23-005{sufixo_freio}'
            elif kw == "3.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-030-23-005{sufixo_freio}'
            elif kw == "4.4":
                chave_gerada = f'{base_material}-{modelo_chave}-F-044-72-005{sufixo_freio}'
            elif kw == "5.5":
                chave_gerada = f'{base_material}-{modelo_chave}-F-055-72-005{sufixo_freio}'
            else:
                print("Configuração de Kw não encontrada para 220V.")
                return
        else:
            if kw == "0.4":
                chave_gerada = f'{base_material}-{modelo_chave}-B-004-36-005-W{sufixo_freio}'
            elif kw == "0.75":
                chave_gerada = f'{base_material}-{modelo_chave}-C-008-36-005-W{sufixo_freio}'
            elif kw == "1.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-010-23-005-W{sufixo_freio}'
            elif kw == "1.2":
                chave_gerada = f'{base_material}-{modelo_chave}-E-012-35-005-W{sufixo_freio}'
            elif kw == "2.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-020-23-005-Y{sufixo_freio}'
            elif kw == "3.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-030-23-005-Y{sufixo_freio}'
            elif kw == "4.4":
                chave_gerada = f'{base_material}-{modelo_chave}-F-044-72-005-Y{sufixo_freio}'
            elif kw == "5.5":
                chave_gerada = f'{base_material}-{modelo_chave}-F-055-72-005-Y{sufixo_freio}'
            else:
                print("Configuração de Kw não encontrada para 220V.")
                return   
    elif tensao == 380 or tensao == 440:
        if pergunta_freio == 's':
            if kw == "1.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-010-23-005{sufixo_freio}'
            elif kw == "2.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-020-23-005{sufixo_freio}'
            elif kw == "3.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-030-23-005{sufixo_freio}'
            elif kw == "4.4":
                chave_gerada = f'{base_material}-{modelo_chave}-E-044-73-005{sufixo_freio}'
            elif kw == "5.5":
                chave_gerada = f'{base_material}-{modelo_chave}-E-055-73-005{sufixo_freio}'
            elif kw == "7.5":
                chave_gerada = f'{base_material}-{modelo_chave}-E-075-73-005{sufixo_freio}'
            else:
                print("Configuração de Kw não encontrada para 380V/440V.")
                return
        else:
            if kw == "1.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-010-23-005-W{sufixo_freio}'
            elif kw == "1.2":
                chave_gerada = f'{base_material}-{modelo_chave}-E-012-23-005-W{sufixo_freio}'
            elif kw == "2.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-020-23-005-W{sufixo_freio}'
            elif kw == "3.0":
                chave_gerada = f'{base_material}-{modelo_chave}-E-030-23-005-Y{sufixo_freio}'
            elif kw == "4.4":
                chave_gerada = f'{base_material}-{modelo_chave}-E-044-73-005-Y{sufixo_freio}'
            elif kw == "5.5":
                chave_gerada = f'{base_material}-{modelo_chave}-E-055-73-005-Y{sufixo_freio}'
            elif kw == "7.5":
                chave_gerada = f'{base_material}-{modelo_chave}-E-075-73-005-Y{sufixo_freio}'
            else:
                print("Configuração de Kw não encontrada para 380V/440V.")
                return   
    else:
        print("Tensão inválida.")
        return

    # Chave final gerada
    print(f"Chave gerada: {chave_gerada}")  # Debug: Verificar a chave gerada

    # Agora buscamos essa chave no dicionário correspondente
    quantidade = int(input('Digite a quantidade do material: '))
    valor = converter_valor(input('Digite o valor do item com IPI: '))
    valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
    valor_quantidade = valor * quantidade
    
    if tensao == 220:
        modelo, descricao_material = busca_kit220v(chave_gerada)
    elif tensao == 380 or tensao == 440:
        modelo, descricao_material = busca_kit380v(chave_gerada)

    if not modelo:
        print('\nMaterial não encontrado.\n')
    
    if valor_IPI != '0':
        valor_final_c_ipi = conta_IPI(valor, valor_IPI)
    else:
        valor_final_c_ipi = valor

    materiais.append({
        'modelo': modelo,
        'descricao_material': descricao_material,
        'quantidade': quantidade,
        'valor_final_c_ipi': valor_final_c_ipi,
        'valor_IPI': valor_IPI,
        'valor_quantidade': valor_quantidade
    })

def outros_materiais(materiais):
    modelo = input('Digite o nome do material: ')
    descricao_material = input("Digite a descrição do material: ")
    quantidade = int(input('Digite a quantidade do material: '))
    valor = converter_valor(input('Digite o valor do item com IPI: '))
    valor_IPI = input('Digite o valor do IPI (0, 3,25, 6,5, 9,75): ')
    valor_quantidade = valor * quantidade

    if valor_IPI != '0':
        valor_final_c_ipi = conta_IPI(valor, valor_IPI)
    else:
        valor_final_c_ipi = valor

    materiais.append({
    'modelo': modelo,
    'descricao_material': descricao_material,
    'quantidade': quantidade,
    'valor_final_c_ipi': valor_final_c_ipi,
    'valor_IPI': valor_IPI,
    'valor_quantidade': valor_quantidade
    })

#===================================ORÇAMENTOS===================================

def orcamentos_email():
    cliente = input('Digite o nome do cliente: ')
    quantidade_cotacao = int(input("Quantos materiais serão cotados?: "))
    forma_pagamento = input("Digite a forma de pagamento: ")
    materiais = []

    for _ in range(quantidade_cotacao):
        menu_materiais(materiais)
        
    texto_orcamento = texto_orcamento_email(cliente, forma_pagamento, materiais)
    enviar_email_pyautogui(texto_orcamento)

def orcamentos_whats():
    cliente = input('Digite o nome do cliente: ')
    quantidade_cotacao = int(input("Quantos materiais serão cotados?: "))
    forma_pagamento = input("Digite a forma de pagamento: ")
    materiais = []

    for _ in range(quantidade_cotacao):
        menu_materiais(materiais)
       

    texto_orcamento = texto_orcamento_wsp(cliente, forma_pagamento, materiais)
    enviar_wsp_pyautogui(texto_orcamento)

#===================================ENVIAR ORÇAMENTO===================================

def enviar_email_pyautogui(texto_orcamento):
    pyperclip.copy(texto_orcamento)
    time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.click(x=1273, y=282)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')

def enviar_wsp_pyautogui(texto_orcamento):
    pyperclip.copy(texto_orcamento)
    time.sleep(2)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')


#===================================FORMATAR PARA VALOR/TEXTO===================================

def formatar_valor(valor):
    return f"{valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')

def formata_cv(cv):
    # Formata o valor do CV para o formato padrão
    return f"{cv.replace(',', '.')}CV".upper()

def formata_descricao(descricao):
   # Remove espaços e converte a descrição para maiúsculas 
    return descricao.replace(' ', '').replace(',', '.').upper()

def converter_valor(valor_str):
    # Substitui vírgula por ponto
    valor_str = valor_str.replace(',', '.')
    # Converte para float
    return float(valor_str)

#===================================FIM===================================
