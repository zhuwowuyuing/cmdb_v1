cmdb_v1

Required Python module:
Django==1.6.2
MySQL-python==1.2.5
South==1.0.0



#迁移数据

SELECT * FROM assets.assets_status

SELECT * FROM assets_v1.assets_status

INSERT INTO assets_v1.assets_status
SELECT * FROM assets.assets_status

SELECT * FROM assets.assets_servers
SELECT * FROM assets_v1.assets_devices

INSERT INTO assets_v1.assets_devices
SELECT asset,asset_old,district,company,status_id,TYPE,subtype,manufacturer,model,serialno FROM assets.assets_servers

SELECT * FROM assets_v1.assets_server

INSERT INTO assets_v1.assets_server
SELECT asset,size,cpu,harddisk,ram,os,building,location,consignee,hostname,dept,business,ownername,warehousedate,receivedate,warrantyexpirationdate,scrapDate,changeInfo,asset
FROM assets.assets_servers