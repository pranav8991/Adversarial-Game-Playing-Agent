from sample_players import DataPlayer
import math
class CustomPlayer(DataPlayer):
    def area(self, change_1, change_2):
        value_1 = change_1 // 13 
        new_value_1 = change_1 % 13
        value_2 = change_2 // 13
        new_value_2 = change_2 % 13
        dis = math.sqrt((value_1 - value_2)**2 + (new_value_1 - new_value_2) **2)
        return dis
    def new_area(self, change_1):
        value_1 = change_1 // 13 
        new_value_1 = change_1 % 13
        left = value_1 
        right = 13 - value_1 
        up = new_value_1 
        bottom = 10 - new_value_1
        dis = min(left, right, up, bottom) + 1
        return dis
    def final_answer(self, cond):
        change_org = cond.locs[self.player_id]
        change_1_org = cond.liberties(change_org)
        change_2_org = cond.locs[1 - self.player_id]
        change_liberties = cond.liberties(change_2_org)
        change_liberties_unique = [m for m in change_1_org if m not in change_liberties]
        final_liberties = []
        for next_step in change_liberties_unique:
            final_liberty = cond.liberties(next_step)
            final_liberties.extend(final_liberty)
        final_liberties = set(final_liberties)
        areas = 0
        areas_opp = 0
        for change in final_liberties:
            distance_opp = self.area(change, change_2_org)
            areas += distance_opp
        for change in change_liberties:
            distance_opp = self.area(change, change_org)
            areas_opp += distance_opp  
        final_answer = areas / (areas_opp + 0.001)
        return final_answer
    def get_action(self, cond):
        import random
        self.queue.put(max(cond.actions(), key=lambda m: self.final_answer(cond.result(m))))