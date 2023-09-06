import os

from dotenv import load_dotenv
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    Integer,
    PrimaryKeyConstraint,
    String,
    create_engine,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

load_dotenv()
RDS_ENDPOINT = os.environ.get("RDS_ENDPOINT")
RDS_PASSWORD = os.environ.get("RDS_PASSWORD")


Base = declarative_base()


class AllFeaturesJSONTable(Base):
    __tablename__ = "all_features_json"
    __table_args__ = (PrimaryKeyConstraint("game_id"),)
    game_id = Column(String)
    data = Column(JSONB)


class PredictionsTable(Base):
    __tablename__ = "predictions"
    __table_args__ = (PrimaryKeyConstraint("game_id", "prediction_datetime"),)
    game_id = Column(String)
    prediction_datetime = Column(DateTime)
    open_line_hv = Column(Float)
    prediction_line_hv = Column(Float)
    ml_cls_rating_hv = Column(Float)
    game_rating_hv = Column(Float)
    prediction_direction = Column(String)
    directional_game_rating = Column(Float)
    ml_reg_pred_1 = Column(Float)
    ml_reg_pred_2 = Column(Float)
    ml_cls_pred_1 = Column(Float)
    ml_cls_pred_2 = Column(Float)
    ml_cls_prob_1 = Column(Float)
    ml_cls_prob_2 = Column(Float)
    dl_reg_pred_1 = Column(Float)
    dl_reg_pred_2 = Column(Float)
    dl_cls_pred_1 = Column(Float)
    dl_cls_pred_2 = Column(Float)
    dl_cls_prob_1 = Column(Float)
    dl_cls_prob_2 = Column(Float)


class GamesTable(Base):
    __tablename__ = "games"
    __table_args__ = (PrimaryKeyConstraint("game_id"),)

    game_id = Column(String)
    game_datetime = Column(DateTime)
    home_team = Column(String)
    away_team = Column(String)
    open_line = Column(Float)
    home_score = Column(Integer)
    away_score = Column(Integer)
    game_completed = Column(Boolean)
    scores_last_update = Column(DateTime)
    odds_last_update = Column(DateTime)


class LinesTable(Base):
    __tablename__ = "lines"
    __table_args__ = (PrimaryKeyConstraint("game_id", "line_datetime"),)

    game_id = Column(String)
    line_datetime = Column(DateTime)
    # Columns for each bookmaker
    # Barstool Sportsbook
    barstool_home_line = Column(Float)
    barstool_home_line_price = Column(Float)
    barstool_away_line = Column(Float)
    barstool_away_line_price = Column(Float)

    # BetOnline.ag
    betonlineag_home_line = Column(Float)
    betonlineag_home_line_price = Column(Float)
    betonlineag_away_line = Column(Float)
    betonlineag_away_line_price = Column(Float)

    # BetMGM
    betmgm_home_line = Column(Float)
    betmgm_home_line_price = Column(Float)
    betmgm_away_line = Column(Float)
    betmgm_away_line_price = Column(Float)

    # BetRivers
    betrivers_home_line = Column(Float)
    betrivers_home_line_price = Column(Float)
    betrivers_away_line = Column(Float)
    betrivers_away_line_price = Column(Float)

    # BetUS
    betus_home_line = Column(Float)
    betus_home_line_price = Column(Float)
    betus_away_line = Column(Float)
    betus_away_line_price = Column(Float)

    # Bovada
    bovada_home_line = Column(Float)
    bovada_home_line_price = Column(Float)
    bovada_away_line = Column(Float)
    bovada_away_line_price = Column(Float)

    # DraftKings
    draftkings_home_line = Column(Float)
    draftkings_home_line_price = Column(Float)
    draftkings_away_line = Column(Float)
    draftkings_away_line_price = Column(Float)

    # FanDuel
    fanduel_home_line = Column(Float)
    fanduel_home_line_price = Column(Float)
    fanduel_away_line = Column(Float)
    fanduel_away_line_price = Column(Float)

    # LowVig.ag
    lowvig_home_line = Column(Float)
    lowvig_home_line_price = Column(Float)
    lowvig_away_line = Column(Float)
    lowvig_away_line_price = Column(Float)

    # MyBookie.ag
    mybookieag_home_line = Column(Float)
    mybookieag_home_line_price = Column(Float)
    mybookieag_away_line = Column(Float)
    mybookieag_away_line_price = Column(Float)

    # PointsBet (US)
    pointsbetus_home_line = Column(Float)
    pointsbetus_home_line_price = Column(Float)
    pointsbetus_away_line = Column(Float)
    pointsbetus_away_line_price = Column(Float)

    # SuperBook
    superbook_home_line = Column(Float)
    superbook_home_line_price = Column(Float)
    superbook_away_line = Column(Float)
    superbook_away_line_price = Column(Float)

    # TwinSpires
    twinspires_home_line = Column(Float)
    twinspires_home_line_price = Column(Float)
    twinspires_away_line = Column(Float)
    twinspires_away_line_price = Column(Float)

    # Unibet
    unibet_us_home_line = Column(Float)
    unibet_us_home_line_price = Column(Float)
    unibet_us_away_line = Column(Float)
    unibet_us_away_line_price = Column(Float)

    # William Hill (Caesars)
    williamhill_us_home_line = Column(Float)
    williamhill_us_home_line_price = Column(Float)
    williamhill_us_away_line = Column(Float)
    williamhill_us_away_line_price = Column(Float)

    # WynnBET
    wynnbet_home_line = Column(Float)
    wynnbet_home_line_price = Column(Float)
    wynnbet_away_line = Column(Float)
    wynnbet_away_line_price = Column(Float)


class NbaStatsPlayerGeneralTraditionalTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_traditional"
    __table_args__ = (PrimaryKeyConstraint("player_id", "to_date", "season_type"),)

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    tov = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    nba_fantasy_pts = Column(Float)
    dd2 = Column(Integer)
    td3 = Column(Integer)


class NbaStatsPlayerGeneralAdvancedTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_advanced"
    __table_args__ = (PrimaryKeyConstraint("player_id", "to_date", "season_type"),)

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    e_off_rating = Column(Float)
    off_rating = Column(Float)
    sp_work_off_rating = Column(Float)
    e_def_rating = Column(Float)
    def_rating = Column(Float)
    sp_work_def_rating = Column(Float)
    e_net_rating = Column(Float)
    net_rating = Column(Float)
    sp_work_net_rating = Column(Float)
    ast_pct = Column(Float)
    ast_to = Column(Float)
    ast_ratio = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    reb_pct = Column(Float)
    tm_tov_pct = Column(Float)
    e_tov_pct = Column(Float)
    efg_pct = Column(Float)
    ts_pct = Column(Float)
    usg_pct = Column(Float)
    e_usg_pct = Column(Float)
    e_pace = Column(Float)
    pace = Column(Float)
    pace_per40 = Column(Float)
    sp_work_pace = Column(Float)
    pie = Column(Float)
    poss = Column(Integer)
    fgm = Column(Integer)
    fga = Column(Integer)
    fgm_pg = Column(Float)
    fga_pg = Column(Float)
    fg_pct = Column(Float)


class NbaStatsPlayerGeneralMiscTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_misc"
    __table_args__ = (PrimaryKeyConstraint("player_id", "to_date", "season_type"),)

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    pts_off_tov = Column(Float)
    pts_2nd_chance = Column(Float)
    pts_fb = Column(Float)
    pts_paint = Column(Float)
    opp_pts_off_tov = Column(Float)
    opp_pts_2nd_chance = Column(Float)
    opp_pts_fb = Column(Float)
    opp_pts_paint = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    nba_fantasy_pts = Column(Float)


class NbaStatsPlayerGeneralScoringTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_scoring"
    __table_args__ = (PrimaryKeyConstraint("player_id", "to_date", "season_type"),)

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    pct_fga_2pt = Column(Float)
    pct_fga_3pt = Column(Float)
    pct_pts_2pt = Column(Float)
    pct_pts_2pt_mr = Column(Float)
    pct_pts_3pt = Column(Float)
    pct_pts_fb = Column(Float)
    pct_pts_ft = Column(Float)
    pct_pts_off_tov = Column(Float)
    pct_pts_paint = Column(Float)
    pct_ast_2pm = Column(Float)
    pct_uast_2pm = Column(Float)
    pct_ast_3pm = Column(Float)
    pct_uast_3pm = Column(Float)
    pct_ast_fgm = Column(Float)
    pct_uast_fgm = Column(Float)
    fgm = Column(Integer)
    fga = Column(Integer)
    fg_pct = Column(Float)


class NbaStatsPlayerGeneralUsageTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_usage"
    __table_args__ = (PrimaryKeyConstraint("player_id", "to_date", "season_type"),)

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    usg_pct = Column(Float)
    pct_fgm = Column(Float)
    pct_fga = Column(Float)
    pct_fg3m = Column(Float)
    pct_fg3a = Column(Float)
    pct_ftm = Column(Float)
    pct_fta = Column(Float)
    pct_oreb = Column(Float)
    pct_dreb = Column(Float)
    pct_reb = Column(Float)
    pct_ast = Column(Float)
    pct_tov = Column(Float)
    pct_stl = Column(Float)
    pct_blk = Column(Float)
    pct_blka = Column(Float)
    pct_pf = Column(Float)
    pct_pfd = Column(Float)
    pct_pts = Column(Float)


class NbaStatsPlayerGeneralOpponentTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_opponent"
    __table_args__ = (
        PrimaryKeyConstraint("vs_player_id", "to_date", "season_type", "team_id"),
    )

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    vs_player_id = Column(Integer)
    vs_player_name = Column(String)
    court_status = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    opp_fgm = Column(Float)
    opp_fga = Column(Float)
    opp_fg_pct = Column(Float)
    opp_fg3m = Column(Float)
    opp_fg3a = Column(Float)
    opp_fg3_pct = Column(Float)
    opp_ftm = Column(Float)
    opp_fta = Column(Float)
    opp_ft_pct = Column(Float)
    opp_oreb = Column(Float)
    opp_dreb = Column(Float)
    opp_reb = Column(Float)
    opp_ast = Column(Float)
    opp_tov = Column(Float)
    opp_stl = Column(Float)
    opp_blk = Column(Float)
    opp_blka = Column(Float)
    opp_pf = Column(Float)
    opp_pfd = Column(Float)
    opp_pts = Column(Float)
    plus_minus = Column(Float)


class NbaStatsPlayerGeneralDefenseTable(Base):
    __tablename__ = "ibd_nba_stats_player_general_defense"
    __table_args__ = (PrimaryKeyConstraint("player_id", "to_date", "season_type"),)

    to_date = Column(Date)
    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    nickname = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    age = Column(Integer)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    def_rating = Column(Float)
    dreb = Column(Float)
    dreb_pct = Column(Float)
    pct_dreb = Column(Float)
    stl = Column(Float)
    pct_stl = Column(Float)
    blk = Column(Float)
    pct_blk = Column(Float)
    opp_pts_off_tov = Column(Float)
    opp_pts_2nd_chance = Column(Float)
    opp_pts_fb = Column(Float)
    opp_pts_paint = Column(Float)
    def_ws = Column(Float)


class NbaStatsBoxscoresTraditionalTable(Base):
    __tablename__ = "ibd_nba_stats_boxscores_traditional"
    __table_args__ = (PrimaryKeyConstraint("player_id", "game_date"),)

    season = Column(String)
    season_type = Column(String)
    player = Column(String)
    player_id = Column(Integer)
    team = Column(String)
    team_id = Column(Integer)
    game_id = Column(String)
    match_up = Column(String)
    game_date = Column(Date)
    w_l = Column(String)
    min = Column(Integer)
    pts = Column(Integer)
    fgm = Column(Integer)
    fga = Column(Integer)
    fg_pct = Column(Float)
    three_pm = Column(Integer)
    three_pa = Column(Integer)
    three_p_pct = Column(Float)
    ftm = Column(Integer)
    fta = Column(Integer)
    ft_pct = Column(Float)
    oreb = Column(Integer)
    dreb = Column(Integer)
    reb = Column(Integer)
    ast = Column(Integer)
    stl = Column(Integer)
    blk = Column(Integer)
    tov = Column(Integer)
    pf = Column(Integer)
    plus_minus = Column(Integer)
    fp = Column(Float)


class NbaStatsBoxscoresAdvTraditionalTable(Base):
    __tablename__ = "ibd_nba_stats_boxscores_adv_traditional"
    __table_args__ = (PrimaryKeyConstraint("player_id", "game_date"),)

    season_year = Column(String)
    season_type = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    nickname = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(Date)
    matchup = Column(String)
    w_l = Column(String)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    three_pm = Column(Float)
    three_pa = Column(Float)
    three_p_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    tov = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)
    nba_fantasy_pts = Column(Float)
    dd2 = Column(Float)
    td3 = Column(Float)


class NbaStatsBoxscoresAdvAdvancedTable(Base):
    __tablename__ = "ibd_nba_stats_boxscores_adv_advanced"
    __table_args__ = (PrimaryKeyConstraint("player_id", "game_date"),)

    season_type = Column(String)
    season_year = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    nickname = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(Date)
    matchup = Column(String)
    w_l = Column(String)
    min = Column(Float)
    e_off_rating = Column(Float)
    off_rating = Column(Float)
    sp_work_off_rating = Column(Float)
    e_def_rating = Column(Float)
    def_rating = Column(Float)
    sp_work_def_rating = Column(Float)
    e_net_rating = Column(Float)
    net_rating = Column(Float)
    sp_work_net_rating = Column(Float)
    ast_pct = Column(Float)
    ast_to = Column(Float)
    ast_ratio = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    reb_pct = Column(Float)
    tm_tov_pct = Column(Float)
    e_tov_pct = Column(Float)
    efg_pct = Column(Float)
    ts_pct = Column(Float)
    usg_pct = Column(Float)
    e_usg_pct = Column(Float)
    e_pace = Column(Float)
    pace = Column(Float)
    pace_per40 = Column(Float)
    sp_work_pace = Column(Float)
    pie = Column(Float)
    poss = Column(Integer)
    fgm = Column(Integer)
    fga = Column(Integer)
    fgm_pg = Column(Float)
    fga_pg = Column(Float)
    fg_pct = Column(Float)


class NbaStatsBoxscoresAdvMiscTable(Base):
    __tablename__ = "ibd_nba_stats_boxscores_adv_misc"
    __table_args__ = (PrimaryKeyConstraint("player_id", "game_date"),)

    season_type = Column(String)
    season_year = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    nickname = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(Date)
    matchup = Column(String)
    w_l = Column(String)
    min = Column(Float)
    pts_off_tov = Column(Integer)
    pts_2nd_chance = Column(Integer)
    pts_fb = Column(Integer)
    pts_paint = Column(Integer)
    opp_pts_off_tov = Column(Integer)
    opp_pts_2nd_chance = Column(Integer)
    opp_pts_fb = Column(Integer)
    opp_pts_paint = Column(Integer)
    blk = Column(Integer)
    blka = Column(Integer)
    pf = Column(Integer)
    pfd = Column(Integer)
    nba_fantasy_pts = Column(Float)


class NbaStatsBoxscoresAdvScoringTable(Base):
    __tablename__ = "ibd_nba_stats_boxscores_adv_scoring"
    __table_args__ = (PrimaryKeyConstraint("player_id", "game_date"),)

    season_type = Column(String)
    season_year = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    nickname = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(Date)
    matchup = Column(String)
    w_l = Column(String)
    min = Column(Float)
    pct_fga_2pt = Column(Float)
    pct_fga_3pt = Column(Float)
    pct_pts_2pt = Column(Float)
    pct_pts_2pt_mr = Column(Float)
    pct_pts_3pt = Column(Float)
    pct_pts_fb = Column(Float)
    pct_pts_ft = Column(Float)
    pct_pts_off_tov = Column(Float)
    pct_pts_paint = Column(Float)
    pct_ast_2pm = Column(Float)
    pct_uast_2pm = Column(Float)
    pct_ast_3pm = Column(Float)
    pct_uast_3pm = Column(Float)
    pct_ast_fgm = Column(Float)
    pct_uast_fgm = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)


class NbaStatsBoxscoresAdvUsageTable(Base):
    __tablename__ = "ibd_nba_stats_boxscores_adv_usage"
    __table_args__ = (PrimaryKeyConstraint("player_id", "game_date"),)

    season_type = Column(String)
    season_year = Column(String)
    player_id = Column(Integer)
    player_name = Column(String)
    nickname = Column(String)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    team_name = Column(String)
    game_id = Column(String)
    game_date = Column(Date)
    matchup = Column(String)
    w_l = Column(String)
    min = Column(Integer)
    usg_pct = Column(Float)
    pct_fgm = Column(Float)
    pct_fga = Column(Float)
    pct_fg3m = Column(Float)
    pct_fg3a = Column(Float)
    pct_ftm = Column(Float)
    pct_fta = Column(Float)
    pct_oreb = Column(Float)
    pct_dreb = Column(Float)
    pct_reb = Column(Float)
    pct_ast = Column(Float)
    pct_tov = Column(Float)
    pct_stl = Column(Float)
    pct_blk = Column(Float)
    pct_blka = Column(Float)
    pct_pf = Column(Float)
    pct_pfd = Column(Float)
    pct_pts = Column(Float)


class FivethirtyeightPlayerTable(Base):
    __tablename__ = "ibd_fivethirtyeight_player"
    __table_args__ = (PrimaryKeyConstraint("player_id", "season", "to_date"),)
    to_date = Column(Date)
    player_name = Column(String)
    player_id = Column(String)
    season = Column(Integer)
    poss = Column(Integer)
    mp = Column(Integer)
    raptor_box_offense = Column(Float)
    raptor_box_defense = Column(Float)
    raptor_box_total = Column(Float)
    raptor_onoff_offense = Column(Float)
    raptor_onoff_defense = Column(Float)
    raptor_onoff_total = Column(Float)
    raptor_offense = Column(Float)
    raptor_defense = Column(Float)
    raptor_total = Column(Float)
    war_total = Column(Float)
    war_reg_season = Column(Float)
    war_playoffs = Column(Float)
    predator_offense = Column(Float)
    predator_defense = Column(Float)
    predator_total = Column(Float)
    pace_impact = Column(Float)


class NbastatsGeneralTraditionalTable(Base):
    """
    Data source provider: nbastats
    Data source URL: https://www.nba.com/stats/teams/traditional
    Data source description:
    """

    __tablename__ = "team_nbastats_general_traditional"
    __table_args__ = (PrimaryKeyConstraint("team_name", "to_date", "games"),)
    team_name = Column(String)
    to_date = Column(Date)
    season = Column(String)
    season_type = Column(String)
    games = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)
    fg_pct = Column(Float)
    fg3m = Column(Float)
    fg3a = Column(Float)
    fg3_pct = Column(Float)
    ftm = Column(Float)
    fta = Column(Float)
    ft_pct = Column(Float)
    oreb = Column(Float)
    dreb = Column(Float)
    reb = Column(Float)
    ast = Column(Float)
    tov = Column(Float)
    stl = Column(Float)
    blk = Column(Float)
    blka = Column(Float)
    pf = Column(Float)
    pfd = Column(Float)
    pts = Column(Float)
    plus_minus = Column(Float)


class NbastatsGeneralAdvancedTable(Base):
    """
    Data source provider: nbastats
    Data source URL: https://www.nba.com/stats/teams/advanced
    Data source description:
    """

    __tablename__ = "team_nbastats_general_advanced"
    __table_args__ = (PrimaryKeyConstraint("team_name", "to_date", "games"),)
    team_name = Column(String)
    to_date = Column(Date)
    season = Column(String)
    season_type = Column(String)
    games = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    e_off_rating = Column(Float)
    off_rating = Column(Float)
    e_def_rating = Column(Float)
    def_rating = Column(Float)
    e_net_rating = Column(Float)
    net_rating = Column(Float)
    ast_pct = Column(Float)
    ast_to = Column(Float)
    ast_ratio = Column(Float)
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    reb_pct = Column(Float)
    tm_tov_pct = Column(Float)
    efg_pct = Column(Float)
    ts_pct = Column(Float)
    e_pace = Column(Float)
    pace = Column(Float)
    pace_per40 = Column(Float)
    poss = Column(Integer)
    pie = Column(Float)


class NbastatsGeneralFourfactorsTable(Base):
    """
    Data source provider: nbastats
    Data source URL: https://www.nba.com/stats/teams/four-factors
    Data source description:
    """

    __tablename__ = "team_nbastats_general_fourfactors"
    __table_args__ = (PrimaryKeyConstraint("team_name", "to_date", "games"),)
    team_name = Column(String)
    to_date = Column(Date)
    season = Column(String)
    season_type = Column(String)
    games = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    efg_pct = Column(Float)
    fta_rate = Column(Float)
    tm_tov_pct = Column(Float)
    oreb_pct = Column(Float)
    opp_efg_pct = Column(Float)
    opp_fta_rate = Column(Float)
    opp_tov_pct = Column(Float)
    opp_oreb_pct = Column(Float)


class NbastatsGeneralOpponentTable(Base):
    """
    Data source provider: nbastats
    Data source URL: https://www.nba.com/stats/teams/opponent
    Data source description:
    """

    __tablename__ = "team_nbastats_general_opponent"
    __table_args__ = (PrimaryKeyConstraint("team_name", "to_date", "games"),)
    team_name = Column(String)
    to_date = Column(Date)
    season = Column(String)
    season_type = Column(String)
    games = Column(String)
    gp = Column(Integer)
    w = Column(Integer)
    l = Column(Integer)
    w_pct = Column(Float)
    min = Column(Float)
    opp_fgm = Column(Float)
    opp_fga = Column(Float)
    opp_fg_pct = Column(Float)
    opp_fg3m = Column(Float)
    opp_fg3a = Column(Float)
    opp_fg3_pct = Column(Float)
    opp_ftm = Column(Float)
    opp_fta = Column(Float)
    opp_ft_pct = Column(Float)
    opp_oreb = Column(Float)
    opp_dreb = Column(Float)
    opp_reb = Column(Float)
    opp_ast = Column(Float)
    opp_tov = Column(Float)
    opp_stl = Column(Float)
    opp_blk = Column(Float)
    opp_blka = Column(Float)
    opp_pf = Column(Float)
    opp_pfd = Column(Float)
    opp_pts = Column(Float)
    plus_minus = Column(Float)


class FivethirtyeightGamesTable(Base):
    """
    Data source provider: fivethirtyeight
    Data source URL: https://projects.fivethirtyeight.com/nba-model/nba_elo.csv
    Data source description: CSV file going back to 1947. Also includes game scores.
    """

    __tablename__ = "team_fivethirtyeight_games"
    __table_args__ = (PrimaryKeyConstraint("date", "team1", "team2"),)
    date = Column(Date)
    season = Column(String)
    neutral = Column(Boolean)
    season_type = Column(String)
    team1 = Column(String)
    team2 = Column(String)
    elo1_pre = Column(Float)
    elo2_pre = Column(Float)
    elo_prob1 = Column(Float)
    elo_prob2 = Column(Float)
    elo1_post = Column(Float)
    elo2_post = Column(Float)
    carm_elo1_pre = Column(Float)
    carm_elo2_pre = Column(Float)
    carm_elo_prob1 = Column(Float)
    carm_elo_prob2 = Column(Float)
    carm_elo1_post = Column(Float)
    carm_elo2_post = Column(Float)
    raptor1_pre = Column(Float)
    raptor2_pre = Column(Float)
    raptor_prob1 = Column(Float)
    raptor_prob2 = Column(Float)
    score1 = Column(Float)
    score2 = Column(Float)
    quality = Column(Float)
    importance = Column(Float)
    total_rating = Column(Float)


if __name__ == "__main__":
    # Creates all database tables defined above that haven't been created yet.
    engine = create_engine(
        f"postgresql://postgres:{RDS_PASSWORD}@{RDS_ENDPOINT}/nba_betting"
    )
    Base.metadata.create_all(engine)
