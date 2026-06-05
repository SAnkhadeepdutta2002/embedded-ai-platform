unsigned long packet_id = 0;

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  packet_id++;

  String payload = "TEMP:28";

  String packet =
      "AA55|" +
      String(packet_id) +
      "|" +
      payload +
      "|1234";

  Serial.println(packet);

  delay(1000);
}