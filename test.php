<html>
<head>
	<meta charset="utf-8">
	<script src="jquery-3.5.1.js"></script>
	<script src="../report app/common/vue.js"></script>
</head>
<body>
	<div id="container">
	</div>
	<?php
	// include_once("ajax.php");
	function f($number){
		if($number == 0)
		{
			return 1;
		}
		else
		{
			return ($number * f($number-1));
		};
	};
	function my_f($number){
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
	$start_time = microtime(true);

	$end_time = microtime(true);
	echo "<br> exec time was : ".($end_time-$start_time);
	?>
</body>

</html>