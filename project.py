def run ():
    import pandas as pd
    cost1 = pd.read_csv('Bilding App Cost.csv')
    Servise_list = list(cost1.keys())
    print('Hello \nWelcome to Building Management APP\nPlease select your service by help from the bottom legend and type it.')
    def start():

        print('\n\n'+'{} to Service\n"Remove" to remove\n"Finish" to save and finish\n"Now" to get report'.format(Servise_list))
        Service = input('What is your service?\n: ').title()
        if Service == 'Now':
            print(cost1.to_csv)
            start()
        elif Service == 'Finish':
            return cost1.to_csv('Bilding App Cost.csv',index=False)
        elif Service == 'Remove':
            remove_service = input('What service you want to remove?\n: ').lower().title()
            respance = input('Are you certain to remove "{}" with "{}" cost? yes or no?\n: '.format(remove_service, cost[remove_service][0])).title()
            if respance == 'Yes':
                del cost[remove_service]
                del cost1[remove_service]
                del Servise_list[Servise_list.index(remove_service)]
            start()
        else:
            Cost = input('what is it cost?\n: ')
            respance = input('Your service is \"{}\" with \"{}\" cost.\n This is True? Yes or No? \n: '.format(Service,Cost)).title()
            if respance == 'Yes':
                if Service in Servise_list:
                    cost1[Service][0] += eval(Cost)
                else:
                    Servise_list.append(Service)
                    cost1[Service] = eval(Cost)
            start()
