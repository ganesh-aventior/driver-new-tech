# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base_model import BaseModel


class Variable(BaseModel):

    attributes = [
        'id', 'calcs_fatalities_groups_id', 'countries_id', 'analysis_period', 'smoothing_type',
        'survey_interval',
        'driving_side',
        'discount_rate',
        'return_rate',
        'value_of_life',
        'value_of_life_multiplier',
        'value_of_serious_injury',
        'value_of_serious_injury_multiplier',
        'injury_fatality_ratio',
        'qualification_criteria',
        'qualification_value',
        'traffic_volume_growth_percent_car',
        'traffic_volume_growth_percent_motorcycle',
        'traffic_volume_growth_percent_bicycle',
        'traffic_volume_growth_percent_pedestrian',
        'annual_fatality_growth_exponent',
        'car_run_off_loc_driver_side_calibration_factor',
        'car_run_off_loc_driver_side_aadt_multiplier',
        'car_run_off_loc_driver_side_aadt_power',
        'car_run_off_loc_passenger_side_calibration_factor',
        'car_run_off_loc_passenger_side_aadt_multiplier',
        'car_run_off_loc_passenger_side_aadt_power',
        'car_head_on_loc_calibration_factor',
        'car_head_on_loc_aadt_multiplier',
        'car_head_on_loc_aadt_power',
        'car_head_on_overtaking_calibration_factor',
        'car_head_on_overtaking_aadt_multiplier',
        'car_head_on_overtaking_aadt_power',
        'car_intersection_calibration_factor',
        'car_intersection_aadt_multiplier',
        'car_intersection_aadt_power',
        'car_property_access_calibration_factor',
        'car_property_access_aadt_multiplier',
        'car_property_access_aadt_power',
        'motorcycle_run_off_loc_driver_side_calibration_factor',
        'motorcycle_run_off_loc_driver_side_aadt_multiplier',
        'motorcycle_run_off_loc_driver_side_aadt_power',
        'motorcycle_run_off_loc_passenger_side_calibration_factor',
        'motorcycle_run_off_loc_passenger_side_aadt_multiplier',
        'motorcycle_run_off_loc_passenger_side_aadt_power',
        'motorcycle_head_on_loc_calibration_factor',
        'motorcycle_head_on_loc_aadt_multiplier',
        'motorcycle_head_on_loc_aadt_power',
        'motorcycle_head_on_overtaking_calibration_factor',
        'motorcycle_head_on_overtaking_aadt_multiplier',
        'motorcycle_head_on_overtaking_aadt_power',
        'motorcycle_intersection_calibration_factor',
        'motorcycle_intersection_aadt_multiplier',
        'motorcycle_intersection_aadt_power',
        'motorcycle_property_access_calibration_factor',
        'motorcycle_property_access_aadt_multiplier',
        'motorcycle_property_access_aadt_power',
        'motorcycle_along_calibration_factor',
        'motorcycle_along_aadt_multiplier',
        'motorcycle_along_aadt_power',
        'pedestrian_along_calibration_factor',
        'pedestrian_along_aadt_multiplier',
        'pedestrian_along_aadt_power',
        'pedestrian_crossing_side_road_calibration_factor',
        'pedestrian_crossing_side_road_aadt_multiplier',
        'pedestrian_crossing_side_road_aadt_power',
        'pedestrian_crossing_through_road_calibration_factor',
        'pedestrian_crossing_through_road_aadt_multiplier',
        'pedestrian_crossing_through_road_aadt_power',
        'bicycle_along_calibration_factor',
        'bicycle_along_aadt_multiplier',
        'bicycle_along_aadt_power',
        'bicycle_intersection_calibration_factor',
        'bicycle_intersection_aadt_multiplier',
        'bicycle_intersection_aadt_power',
        'bicycle_run_off_calibration_factor',
        'bicycle_run_off_aadt_multiplier',
        'bicycle_run_off_aadt_power',
        'multi_cm_process',
        'multi_cm_value',
        'gdp',
        'comments_setup',
        'comments_fatality_car',
        'comments_fatality_motorcycle',
        'comments_fatality_pedestrian',
        'comments_fatality_bicycle',
        'comments_economics',
        'comments_countermeasures',
        'comments_growth',
        'comments_other',
        'countermeasure_variables_group',
        'modified_timestamp',
        'car_run_off_loc_driver_side_auto_calibration_target',
        'car_run_off_loc_passenger_side_auto_calibration_target',
        'car_head_on_loc_auto_calibration_target',
        'car_head_on_overtaking_auto_calibration_target',
        'car_intersection_auto_calibration_target',
        'car_property_access_auto_calibration_target',
        'motorcycle_run_off_loc_driver_side_auto_calibration_target',
        'motorcycle_run_off_loc_passenger_side_auto_calibration_target',
        'motorcycle_head_on_loc_auto_calibration_target',
        'motorcycle_head_on_overtaking_auto_calibration_target',
        'motorcycle_intersection_auto_calibration_target',
        'motorcycle_property_access_auto_calibration_target',
        'motorcycle_along_auto_calibration_target',
        'pedestrian_along_auto_calibration_target',
        'pedestrian_crossing_side_road_auto_calibration_target',
        'pedestrian_crossing_through_road_auto_calibration_target',
        'bicycle_along_auto_calibration_target',
        'bicycle_intersection_auto_calibration_target',
        'bicycle_run_off_auto_calibration_target',
        'accredited_supplier_id_coding',
        'stage_2_qa_complete',
        'stage_2_qa_approved_users_id',
        'stage_3_qa_complete',
        'stage_3_qa_approved_users_id',
        'stage_4_qa_complete',
        'stage_4_qa_approved_users_id',
        'stage_5_qa_complete',
        'stage_5_qa_approved_users_id',
        'stage_6_qa_complete',
        'stage_6_qa_approved_users_id',
        'inspection_system_id',
        'accredited_supplier_id_survey',
        'ac_enabled',
        'car_user_group_distribution',
        'car_other_auto_calibration_target',
        'motorcycle_user_group_distribution',
        'motorcycle_other_auto_calibration_target',
        'pedestrian_user_group_distribution',
        'pedestrian_other_auto_calibration_target',
        'bicycle_user_group_distribution',
        'bicycle_other_auto_calibration_target',
        'reported_deaths',
        'sample_period',
        'years_covered_from',
        'years_covered_to',
        'fatality_under_reporting_factor',
        'estimated_number_of_annual_fatals_on_network',
        'fatality_data_source_and_assumptions',
        'cm_pack_id',
        'stage_2_qa_organisation_id',
        'stage_3_qa_organisation_id',
        'stage_4_qa_organisation_id',
        'stage_5_qa_organisation_id',
        'stage_6_qa_organisation_id'
    ]


class VariableForProgramme(BaseModel):
    # same for region, project

    attributes = [
        'land_use_passenger_side',
        'school_zone_crossing_supervisor',
        'intersection_quality',
        'grade',
        'number_of_lanes',
        'roadside_severity_driver_side_distance',
        'roadside_severity_passenger_side_object',
        'truck_speed_limit',
        'motorcycle_observed_flow',
        'land_use_driver_side',
        'roadside_severity_passenger_side_distance',
        'bicycle_star_rating_policy_target',
        'speed_limit',
        'skid_resistance_grip',
        'shoulder_rumble_strips',
        'dataset_id',
        'ped_crossing_facilities_inspected_road',
        'location_id',
        'motorcycle_speed_limit',
        'paved_shoulder_passenger_side',
        'road_name',
        'paved_shoulder_driver_side',
        'intersecting_road_volume',
        'ped_crossing_quality',
        'facilities_for_bicycles',
        'upgrade_cost',
        'bicycle_peak_hour_flow',
        'road_survey_date',
        'intersection_type',
        'centreline_rumble_strips',
        'comments',
        'area_type',
        'ped_star_rating_policy_target',
        'facilities_for_motorised_two_wheelers',
        'coder_name',
        'ped_observed_flow_along_passenger_side',
        'motorcycle_percent',
        'latitude',
        'speed_management',
        'quality_of_curve',
        'image_reference',
        'sidewalk_driver_side',
        'roadside_severity_driver_side_object',
        'annual_fatality_growth_multiplier',
        'coding_date',
        'ped_peak_hour_flow_across',
        'vehicle_flow',
        'carriageway',
        'curvature',
        'ped_observed_flow_along_driver_side',
        'vehicle_star_rating_policy_target',
        'differential_speed_limits',
        'roads_that_cars_can_read',
        'ped_peak_hour_flow_along_driver_side',
        'ped_crossing_facilities_intersecting_road',
        'ped_observed_flow_across',
        'road_condition',
        'operating_speed_85th_percentile',
        'distance',
        'median_type',
        'delineation',
        'ped_peak_hour_flow_along_passenger_side',
        'lane_width',
        'service_road',
        'operating_speed_mean',
        'sight_distance',
        'intersection_channelisation',
        'longitude',
        'ped_fencing',
        'bicycle_observed_flow',
        'property_access_points',
        'length',
        'street_lighting',
        'roadworks',
        'landmark',
        'vehicle_parking',
        'sidewalk_passenger_side',
        'section',
        'school_zone_warning',
        'motorcycle_star_rating_policy_targer'
    ]