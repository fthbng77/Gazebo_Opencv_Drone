# Gazebo_Opencv_Drone
Gazebo dünyasında drone kullanırken gelen gelen görüntünün belli bir kısmı ile işlem yapabilmenizi sağlayacak

Bu kodun yapacakları:
Gazebo dünyasından gelen kamera görüntüleri ile beyaz renk aralığındaki(bunu değiştirebilirsiniz) bir yolu ayırt edebilmenizi ve kameradan gelen görüntünün yalnızca alt bölümünün görüntü işlemeye tabi tutulmasını sağlar.

Bu kod kullanılmadan önce dikkat edilmesi gerekenler:

-Rosun kurulu olduğundan emin olun.
Eğer ROS, ardupilot ya da gazebo kurulu değilse bu repoyu takip edebilirsiniz. Eğer bu repoyu kurmadan yapmaya çalışırsanız çalışmayacaktır.

https://github.com/Intelligent-Quads/iq_tutorials.git

```
git clone https://github.com/fthbng77/Gazebo_Opencv_Drone.git
```
Gazebo_Opencv_Drone dosyasını indirin içinde hazır olarak bir gazebo dünyası var
```
cd
sudo cp /Gazebo_Opencv_Drone/launch/runway_isikli.launch /catkin_ws/src/iq_sim/launch
sudo cp /Gazebo_Opencv_Drone/worlds/rota.world /catkin_ws/src/iq_sim/worlds
```
Ardından gazebo dünyasını açabilirsiniz
```
roslaunch iq_sim runway_isikli.launch
```
başka bir terminalde
```
cd Gazebo_Opencv_Drone
python rota_takip.py
```
