<?php

class week_plan
{
	public $class_rooms = [];
	public $lessons = [];
	public $resists = [
	//day 2-> ring 1 must not be zaban
	//or sum of all zabans must be 22 hours!
	];
	public function __construct()
	{
		
	}
	public function new_class_room_name($class_room_name)
	{
		$tmp = new class_room;
		$this->class_rooms[] = $tmp;
		return $tmp;
	}
	
};
class class_room{
	public $class_room_name;
	public $days = [];
	public function set_name($class_room_name)
	{
		$this->class_room_name = $class_room_name;
	}
	public function new_day()
	{
		$tmp = new day;
		$this->days[] = $tmp;
		return $tmp;
	}
};
class day{
	public $rings = [];
	public function new_ring()
	{
		$tmp = new ring;
		$this->rings[] = $tmp;
		return $tmp;
	}
};
class ring{
	public $value;
	public function set_value($value)
	{
		$this->value = $value;
		echo $this->value;
	}
};
$my_plan = new week_plan;
function build_structure(week_plan $week_plan_instance,$classes_count,$days_count,$rings_count)
{
	$classes = [];
	$days = [];
	$rings = [];
	for($i = 0;$i<$classes_count;$i++)
	{
		$classes[] = $week_plan_instance->new_class_room_name("hamed") ; 
	};
	foreach($classes as $index)
	{
		foreach(range(1,$days_count) as $index_2)
		{
			$new_day = $index->new_day();
			foreach(range(1,$rings_count) as $index_3)
			{
				$new_day->new_ring();
			};
		};
	};
}
build_structure($my_plan,2,2,2);
function check_resist()
{
	
};
function classes_count(week_plan $week_plan_instance)
{
	return count($week_plan_instance->class_rooms);
};
function days_count(week_plan $week_plan_instance,$class_index)
{
	return count($week_plan_instance->class_rooms[$class_index]->days);
};
function rings_count(week_plan $week_plan_instance,$class_index,$day_index)
{
	return count($week_plan_instance->class_rooms[$class_index]->days[$day_index]->rings);
};
function check











