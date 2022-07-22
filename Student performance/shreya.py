#package com.yb.controller;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.lang.reflect.Type;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import com.mysql.jdbc.exceptions.MySQLSyntaxErrorException;
import com.sun.jmx.snmp.Timestamp;
import com.yb.dao.DAOQuires;
import com.yb.dao.DBManager;
import com.yb.exception.DeviceNotFoundException;
import com.yb.service.RemoteService;
import com.yb.to.DeviceTO;
import com.yb.to.HistoryTO;
import com.yb.to.LocationTO;
import com.yb.to.LoginTO;

/*
  Servlet implementation class TrackingController
 
public class Business extends HttpServlet {
	private static final long serialVersionUID = 1L;
    private RemoteService remoteservice;
    private DeviceTO device;
    private LocationTO location;
    private LoginTO login;
    private Gson gson;
    Map<String,String> respMap=null;
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Business() {
      
    	super();
    	remoteservice=new RemoteService();
    	device =new DeviceTO();
    	location =new LocationTO();
    	login=new LoginTO();
    	gson=new Gson();
    	respMap=new HashMap<String,String>();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
			doPost(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		System.out.println("in post controller");
		String responseMsg="";
		String name = request.getParameter("name");
		String email = request.getParameter("email");
		String pass = request.getParameter("password");
		
		String action=request.getParameter("action");
		String actionType=request.getParameter("actionType");
		
		if(action == null)
		{
			
				if(new DAOQuires().checkLogin(email,pass) == null)
				{
					//session.setAttribute("emailid",email);00
					respMap.put("error", "true");
						respMap.put("error_msg", "Unable to Login");
				}
				else{
					respMap.put("error", "false");
					respMap.put("error_msg", "Login Success");
					//session.setAttribute("emailid",email);
				}
				sendResponseToApp(request,response);	
		}
		
		if("register".equals(action))
		{
			new DAOQuires().register(name,email,pass);
			respMap.put("error", "true");
			respMap.put("status", "true");
			sendResponseToApp(request,response);
		}
		if(action.equalsIgnoreCase("CHECK_REG") && action!=null)
		{
			String IMEI=request.getParameter("IMEI");
			device.setIMEI(Long.parseLong(IMEI));
			
			boolean status;
			try {
				status = remoteservice.checkRegStatus(device);
				respMap.put("status", status+"");
				sendResponseToApp(request,response);
			} catch (Exception e) {
				String exception=e.getClass()+"";
				if( exception.contains("CommunicationsException"))
				{
					e.printStackTrace();
					respMap.put("status", "Database disconnected");
				}
				else if( exception.contains("Mysql"))
				{
					e.printStackTrace();
					respMap.put("status", "MySQL Error. Please check server log for more details");
					
				}
				else if( e instanceof DeviceNotFoundException){
					e.printStackTrace();
					respMap.put("status", e.getMessage());
					
				}
				else
				{
					e.printStackTrace();
					respMap.put("status", "Internal Server error. Please check server log for more details");
					
				}
				sendResponseToApp(request,response);
			}
		}
		else if(action.equalsIgnoreCase("LOGIN") && action!=null)
		{
			String username=request.getParameter("username");
			String password=request.getParameter("password");
			
			
			try {
				login = remoteservice.verifyLogin(username, password);
				
				if(login!=null)
				{
					HttpSession session=request.getSession();
					session.setAttribute("login", login);
					response.sendRedirect("dashboard.jsp");
				}
				else
				{
					responseMsg="Invalid username or password";
					request.setAttribute("error", responseMsg);
					RequestDispatcher rd=request.getRequestDispatcher("index.jsp");
					rd.forward(request, response);
				}
			} catch (Exception e) {
				String exception=e.getClass()+"";
				if( exception.contains("CommunicationsException"))
				{
					e.printStackTrace();
					responseMsg="Database disconnected";
				}
				else
				{
					e.printStackTrace();
					responseMsg="Internal Server error. Please check server log for more details";
				}
				request.setAttribute("error", responseMsg);
				RequestDispatcher rd=request.getRequestDispatcher("index.jsp");
				rd.forward(request, response);
			}
			
		}
		else if(action!=null && action.equalsIgnoreCase("CHECK_FIRE"))
		{
			try{
			DBManager dbmanager=new DBManager();
			PreparedStatement ps=dbmanager.getConnection().prepareStatement("select * from fire");
			 ResultSet rs=ps.executeQuery();
			
			 while(rs.next())
			 {
				 
				 respMap.put("status",  rs.getString(1));
				 System.out.println( rs.getString(1));
				 sendResponseToApp(request,response);
			 }
			}catch (Exception e) {
				// TODO: handle exception
				e.printStackTrace();
			}
		
			
		}
		else if(action.equalsIgnoreCase("STORE_INFO") && action!=null)
		{
			device.setReg_name(request.getParameter("emailid"));
			//device.setDevice_type(request.getParameter("type"));
			String IMEI=request.getParameter("imeino");
			device.setIMEI(Long.parseLong(IMEI));		
			login.setFirstName(request.getParameter("name"));
			//login.setLastName(request.getParameter("lastName"));
			login.setPassword(request.getParameter("password"));

			try {
				DBManager dbmanager=new DBManager();
				 String query1="insert into login (username,password,firstname,lastname) values (?,?,?,?)";				 
				 PreparedStatement ps1=dbmanager.getConnection().prepareStatement(query1);				 
				 ps1.setString(1, device.getReg_name());
				 ps1.setString(2, login.getPassword());
				 ps1.setString(3, login.getFirstName());
				 ps1.setString(4, login.getLastName());
				 ps1.execute();
				 sendResponseToApp(request,response);
			} catch (Exception e) {
				String exception=e.getClass()+"";
				if( exception.contains("CommunicationsException"))
				{
					e.printStackTrace();
					respMap.put("status", "Database disconnected");
				}
				else if( exception.contains("Mysql"))
				{
					e.printStackTrace();
					respMap.put("status", "MySQL Error. Please check server log for more details");
					
				}
				else if( e instanceof DeviceNotFoundException){
					e.printStackTrace();
					respMap.put("status", e.getMessage());
					
				}
				else
				{
					e.printStackTrace();
					respMap.put("status", "Internal Server error. Please check server log for more details");
					
				}
				sendResponseToApp(request,response);
			}
			
		}
		else if(action.equalsIgnoreCase("UPDATE_INFO") && action!=null)
		{
			location.setLongitude(Double.parseDouble(request.getParameter("longitude")));
			location.setLatitude(Double.parseDouble(request.getParameter("latitude")));
			
			String IMEI=request.getParameter("IMEI");
			device.setIMEI(Long.parseLong(IMEI));
			
			try {
				DeviceTO deviceResp=remoteservice.updateDeviceLocation(device, location);
				if(deviceResp.isLock() && deviceResp.isLockdone()==false)
				{
					respMap.put("status", "lock");
					respMap.put("pin", deviceResp.getPin()+"");
				}
				else if(deviceResp.isWipeout() && deviceResp.isWipeoutdone()==false)
				{
					respMap.put("status", "wipeout");
				}
				else
				{
					/*
					 * Timestamp time=new Timestamp(); respMap.put("status",
					 * "Location updated :"+time);
					 */
				}
				sendResponseToApp(request,response);
			} catch (Exception e) {
				String exception=e.getClass()+"";
				if( exception.contains("CommunicationsException"))
				{
					e.printStackTrace();
					respMap.put("status", "Database disconnected");
				}
				else if( exception.contains("Mysql"))
				{
					e.printStackTrace();
					respMap.put("status", "MySQL Error. Please check server log for more details");
					
				}
				else if( e instanceof DeviceNotFoundException){
					e.printStackTrace();
					respMap.put("status", e.getMessage());
					
				}
				else
				{
					e.printStackTrace();
					respMap.put("status", "Internal Server error. Please check server log for more details");
					
				}
				sendResponseToApp(request,response);
			}
		}
		else if(action!=null && action.equalsIgnoreCase("LockAndWipe"))
		{ 
		     JsonObject myObj = new JsonObject();
		     boolean adminActionStatus=false;
		     String statusList="";
		     if(request.getParameter("pin")!=null)
		     device.setPin(Integer.parseInt(request.getParameter("pin")));
		     else
		    	 device.setPin(0);	 
			
			
				String adminAction=request.getParameter("adminAction");		
				if(adminAction.equals("lock"))
					{
					device.setLock(true);
					device.setWipeout(false);
					}
				if(adminAction.equals("wipeout"))
					{
					device.setWipeout(true);
					device.setLock(false);
					}
		
			try {
				adminActionStatus=remoteservice.performAdminAction(device);
				if(adminActionStatus)
				{
						myObj.addProperty("success", adminActionStatus);
						if(adminAction.equals("lock"))
						statusList="locking phone successfull";
						if(adminAction.equals("wipeout"))
						statusList="wipe out successfull";
						myObj.addProperty("statusMsg", statusList);
						response.getWriter().write(myObj.toString());
				}
				
				
				
			} catch (Exception e) {
				String exception=e.getClass()+"";
				if( exception.contains("CommunicationsException"))
				{
					e.printStackTrace();
					responseMsg="Database disconnected";
				}
				else if( e.getCause() instanceof MySQLSyntaxErrorException)
				{
					e.printStackTrace();
					responseMsg="MySQL Error. Please check server log for more details";
				}
				else
				{
					e.printStackTrace();
					responseMsg="Internal Server error. Please check server log for more details";
				}
				myObj.addProperty("success", adminActionStatus);
				if(adminAction.equals("lock"))
				statusList="locking phone failed";
				if(adminAction.equals("wipeout"))
				statusList="wipe out failed";
				myObj.addProperty("statusMsg", responseMsg);
				response.getWriter().write(myObj.toString());
			}
		}
		else if(action.equalsIgnoreCase("LOGOUT") && action!=null)
		{
			logout(request);
			response.sendRedirect("index.jsp");
		}
		else
		{
			if(actionType.equalsIgnoreCase("app"))
			{
				System.out.println("INVALID SERVICE CALL APP");
				if(responseMsg=="")
				{
					responseMsg="INVALID SERVICE CALL";
				}
				sendResponseToApp(request,response);
				
			}
			else if(actionType.equalsIgnoreCase("dashboard"))
			{
				System.out.println("INVALID SERVICE CALL DASHBOARD");
				response.sendRedirect("dashboard.jsp");
			}
			else if(actionType.equalsIgnoreCase("index"))
			{
				System.out.println("INVALID SERVICE CALL UI");
				logout(request);
				response.sendRedirect("index.jsp");
			}
			
		}

	}
	
	public void sendResponseToApp(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException
	{		
		try {
			String respString = prepareParametersToSend();
			
			 DataInputStream in = 
		                new DataInputStream((InputStream)request.getInputStream());
		        response.setContentType("text/plain");
		        response.setContentLength(respString.length());
		        PrintWriter out = response.getWriter();
		        out.println(respString);
		        in.close();
		        out.close();
		        out.flush();
		        
		} catch (Exception e) {
			
			e.printStackTrace();
		}
	}
	
	private String prepareParametersToSend() {		
		Type respMapType = new TypeToken<Map<String,String>>() {}.getType();
		return gson.toJson(respMap,respMapType);
	}

	public List<HistoryTO> getHistory(DeviceTO device)
	{
		List<HistoryTO> list=null;
		try {
			list=remoteservice.getHistory(device);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return list;
	}
	
	public void logout(HttpServletRequest request)
	{
		HttpSession session=request.getSession(false);
		if(session!=null)
		session.invalidate();
	}
}