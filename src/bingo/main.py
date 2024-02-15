# Press the green button in the gutter to run the script.
import random

import xlsxwriter

if __name__ == '__main__':
    workbook = xlsxwriter.Workbook('Bingo.xlsx')

    participants = ["Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4", "Joueur 5", "Joueur 6", "Joueur 7", "Joueur 8",
                    "Joueur 9", "Joueur 10", "Joueur 11", "Joueur 12", "Joueur 13"]
    data = ['Github',
            'Git pull',
            'Git merge',
            'Git push',
            'Fastforward',
            'Owner',
            'Trainee',
            'Trainer',
            'Admin rights',
            'Git fetch',
            'Username',
            'Password',
            'Path',
            'Origin',
            'Local',
            'Repository',
            'Branch',
            'Teams',
            'Settings',
            'Workflows',
            'Actions',
            'Git Commit',
            'Submodule',
            'Organisation',
            'Git init',
            'Git log',
            'Git status',
            'Git diff',
            'Git add',
            'Git reset',
            'Git switch',
            'Git tag',
            'Git clone'
            ]

    data.sort()

    style_b = workbook.add_format({"bold": True, "align": "center", "font_size": 16})
    style_i = workbook.add_format({"bold": True, "align": "center", "font_size": 16})
    style_n = workbook.add_format({"bold": True, "align": "center", "font_size": 16})
    style_g = workbook.add_format({"bold": True, "align": "center", "font_size": 16})
    style_o = workbook.add_format({"bold": True, "align": "center", "font_size": 16})

    for joueur in participants:
        worksheet = workbook.add_worksheet(joueur)
        random.shuffle(data)

        for i in range(0, 5):
            offset = i + 10
            worksheet.write('J' + str(offset), data[i])
            worksheet.write('K' + str(offset), data[i + 5])
            worksheet.write('L' + str(offset), data[i + 10])
            worksheet.write('M' + str(offset), data[i + 15])
            worksheet.write('N' + str(offset), data[i + 20])

        worksheet.set_column(9, 13, 15)
        worksheet.set_row(8, None, style_b)

        worksheet.write("J9", "B", style_b)
        worksheet.write("K9", "I", style_i)
        worksheet.write("L9", "N", style_n)
        worksheet.write("M9", "G", style_g)
        worksheet.write("N9", "O", style_o)
        worksheet.add_table("J9:N14", {'autofilter': False,
                                       'style': "Table Style Medium 9",
                                       'columns': [{'header': 'B', "bold": True},
                                                   {'header': 'I'},
                                                   {'header': 'N'},
                                                   {'header': 'G'},
                                                   {'header': 'O'},
                                                   ]})

    workbook.close()
