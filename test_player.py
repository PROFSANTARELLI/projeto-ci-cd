from player import Player 
 
def test_player_damage(): 
    player = Player("Hero", 100) 
    player.take_damage(30) 
    assert player.hp == 70 
 
def test_player_hp_cannot_be_negative(): 
    player = Player("Hero", 10) 
    player.take_damage(50) 
    assert player.hp == 0 
