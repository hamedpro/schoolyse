<pre>
<?php
// class plan{
	// public  $days = [];
	// public function __construct($days_count,$rings_count){
		// for($i = 0;$i<$days_count;$i++){
			// $tmp = new day($rings_count);
			// array_push($this->days,$tmp);
		// };
	// }
// }
// class day{
	// public $rings = [];
	// public function __construct($rings_count){
		// for($i = 0;$i<$rings_count;$i++){
			// $tmp = new ring();
			// array_push($this->rings,$tmp);
		// };
	// }
// }
// class ring{
	// public $name = "hamed";
// }
// $new = new plan(2,3);
// print_r($new->days[0]->rings[0]->name);


// $list = [1,2,3,1];
// $list = array_unique($list);


function factorial($number){
	if($number==0){
		return 1;
	}else{
		$result = 1;
		for($i = 1;$i<($number);$i++){
			$result = $result *( $i + 1);
		};
		return $result;
	};
};
function min_value_plus_one($array){
	//finding index of minimum value of array:
	$index = array_search(min($array),$array);
	$array[$index] += 1;
	return $array;
};
function all($array){
	$results = [];
	
	$sorting_counter = [];
	for($i=0;$i<count($array);$i++){
		$sorting_counter[] = 0;
	};
	
//	while(count($results)!=factorial(count($array))){
	foreach(range(1,9) as $index){
		$tmp = [];
		for($ii = 0;$ii<count($sorting_counter);$ii++){
			$tmp[] = $array[$sorting_counter[$ii]];
			
		};
		print_r($tmp);
		$results[] = $tmp;
		
		$sorting_counter = min_value_plus_one($sorting_counter);
		
	};
};
$results = [];
function permute($list,$l,$r)
{
	if($l == $r)
	{
		//echo $str . "\n";
		//print_r($str);
		global $results;
		$results[] = $list;
	}else{
		for($i = $l;$i <= $r;$i++){
			$str = swap($list,$l,$i);
			permute($list,$l+1,$r);
			$list = swap($list,$l,$i);
		};
	};
};
function swap($list,$i,$j)
{
	$temp;
	$charArray = $list;
	$temp = $charArray[$i];
	$charArray[$i] = $charArray[$j];
	$charArray[$j] = $temp;
	return $charArray;
};
// $start_time = microtime(true);
// $str = [1,2,3,4,5,6,7,8];
// permute($str,0,count($str)-1);
// print_r($results);
// $end_time = microtime(true);
// echo $end_time - $start_time;


class shop{
	public $fruits = [];
}
$my_shop = new shop();
class fruit{
	public $name;
	public function __construct($name){
		$this->name = $name;
		global $my_shop;
		$my_shop->fruits[] = $this;
	}
}
$apple = new fruit("apple");
$orange = new fruit("orange");
$kiwi = new fruit("kiwi");
$orange = new fruit("orange");
foreach($my_shop->fruits as $index){
	echo $index->name;
	echo "<br>";
} 
?>
</pre>